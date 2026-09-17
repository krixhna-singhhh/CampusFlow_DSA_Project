from collections import Counter
from typing import Iterable, List, Tuple

from .models import Resource, Task


def task_subject_distribution(tasks: Iterable[Task]) -> List[Tuple[str, int]]:
    counts = Counter(task.subject for task in tasks)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0].lower()))


def resource_type_distribution(resources: Iterable[Resource]) -> List[Tuple[str, int]]:
    counts = Counter(resource.resource_type for resource in resources)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0].lower()))


def ascii_bar_chart(rows: List[Tuple[str, int]], width: int = 30) -> str:
    if not rows:
        return "No data available."
    max_value = max(value for _, value in rows)
    lines = []
    for label, value in rows:
        bar_len = max(1, round((value / max_value) * width))
        lines.append(f"{label:<18} {'#' * bar_len} {value}")
    return "\n".join(lines)
