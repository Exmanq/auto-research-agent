from __future__ import annotations

import os
from typing import Any

from jinja2 import Template

from .providers.seed import SeedProvider
from .ranker import rank_sources
from .summarizer import extractive_summary, top_keywords

DEFAULT_TOPIC = "LLM Agents: tool use, memory, planning, evals (2024-2026)"


def load_template(path: str) -> Template:
    with open(path, encoding="utf-8") as f:
        return Template(f.read())


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def gather_sources(topic: str, limit: int = 50) -> list[tuple[str, str, float]]:
    providers = [SeedProvider()]
    collected: list[tuple[str, str]] = []
    for provider in providers:
        collected.extend(provider.fetch(topic, limit=limit))
    ranked = rank_sources(topic, collected, top_k=limit)
    return ranked


def summarize_sources(topic: str, ranked_sources: list[tuple[str, str, float]]) -> dict[str, Any]:
    annotations = []
    texts = []
    for url, title, score in ranked_sources:
        annotations.append(f"[{title or url}]({url}) — relevance {score:.2f}")
        texts.append(title or url)
    summary_sents = extractive_summary(topic, texts, max_sentences=8)
    keywords = top_keywords(texts, k=12)
    overview = "\n".join(summary_sents) or "No summary available."
    trends = [f"Growing focus on {kw}" for kw in keywords[:5]]
    declines = [f"Declining emphasis on legacy {kw}" for kw in keywords[5:8]]
    controversies = [f"Debate on {kw} approach effectiveness" for kw in keywords[:5]]
    return {
        "annotations": annotations,
        "overview": overview,
        "keywords": keywords,
        "trends": trends,
        "declines": declines,
        "controversies": controversies,
    }


def generate_ideas(topic: str, keywords: list[str], count: int = 12) -> list[dict[str, str]]:
    base = keywords or ["agents", "tools", "memory", "evals", "planning"]
    ideas: list[dict[str, str]] = []
    seeds = base[:5] if len(base) >= 5 else base * 2
    for i in range(count):
        kw = seeds[i % len(seeds)]
        ideas.append(
            {
                "name": f"{kw.title()} Lab #{i+1}",
                "problem": f"Hard to benchmark {kw} systems consistently",
                "solution": f"Auto pipeline to gather data, run evals, and report {kw} metrics",
                "mvp": "CLI + seed datasets + simple scoring",
                "risks": "Data quality, noisy signals, drift",
            }
        )
    return ideas


def generate_roadmap(topic: str) -> list[str]:
    return [
        "Неделя 1: Обзор источников, выписать ключевые работы и репы",
        "Неделя 2: Пробные запуски библиотек, собрать baseline",
        "Неделя 3: Мини-эксперименты, сравнить подходы",
        "Неделя 4: Свести выводы, оформить демо/отчёт",
    ]


def write_markdown(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")


def render_list(title: str, items: list[str]) -> str:
    lines = [f"# {title}", ""]
    lines.extend([f"- {item}" for item in items])
    return "\n".join(lines)


def run_pipeline(topic: str, out_dir: str):
    ensure_dir(out_dir)
    ranked_sources = gather_sources(topic)
    summary = summarize_sources(topic, ranked_sources)

    sources_lines = [
        f"- [{title or url}]({url}) — score {score:.2f}"
        for url, title, score in ranked_sources
    ]
    write_markdown(
        os.path.join(out_dir, "sources.md"),
        "\n".join(["# Sources", "", *sources_lines]),
    )

    write_markdown(
        os.path.join(out_dir, "tldr.md"),
        render_list("TL;DR", summary["annotations"][:10]),
    )

    deep_template = load_template(
        os.path.join(os.path.dirname(__file__), "templates", "deep_summary.md")
    )
    sections = [
        {"title": "Capabilities", "text": summary["overview"]},
        {"title": "Trends", "text": "\n".join(summary["trends"])},
        {"title": "Declines", "text": "\n".join(summary["declines"])},
    ]
    deep_render = deep_template.render(overview=summary["overview"], sections=sections)
    write_markdown(os.path.join(out_dir, "deep_summary.md"), deep_render)

    write_markdown(os.path.join(out_dir, "trends.md"), render_list("Trends", summary["trends"]))
    write_markdown(
        os.path.join(out_dir, "controversies.md"),
        render_list("Controversies", summary["controversies"]),
    )

    ideas = generate_ideas(topic, summary["keywords"], count=12)
    ideas_template = load_template(os.path.join(os.path.dirname(__file__), "templates", "ideas.md"))
    ideas_render = ideas_template.render(ideas=ideas)
    write_markdown(os.path.join(out_dir, "ideas.md"), ideas_render)

    roadmap = generate_roadmap(topic)
    write_markdown(os.path.join(out_dir, "roadmap.md"), render_list("Roadmap", roadmap))

    return {
        "sources": ranked_sources,
        "summary": summary,
        "ideas": ideas,
        "roadmap": roadmap,
    }
