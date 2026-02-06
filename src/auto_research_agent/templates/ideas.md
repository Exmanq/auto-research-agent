# Project Ideas (10-20)

{% for idea in ideas %}
## {{ loop.index }}. {{ idea.name }}
- Проблема: {{ idea.problem }}
- Решение: {{ idea.solution }}
- MVP: {{ idea.mvp }}
- Риски: {{ idea.risks }}
{% endfor %}
