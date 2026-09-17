from .course_graph import CourseGraph
from .resource_catalog import ResourceCatalog
from .task_manager import TaskManager


def seed_if_empty(task_manager: TaskManager, catalog: ResourceCatalog) -> None:
    if not task_manager.tasks:
        task_manager.add_task("Revise linked lists", "DSA", 5, "2026-09-20", 2.0)
        task_manager.add_task("Practice graph traversal", "DSA", 4, "2026-09-22", 1.5)
        task_manager.add_task("Write lab record", "Programming Lab", 3, "2026-09-24", 1.0)

    if not catalog.resources:
        catalog.add("Graph Algorithms Notes", "BFS DFS shortest path", "Notes", "data/notes/graphs")
        catalog.add("Heap Practice Set", "priority queue heap", "Worksheet", "data/worksheets/heaps")
        catalog.add("Sorting Cheat Sheet", "sorting complexity", "Reference", "data/reference/sorting")


def build_sample_course_graph() -> CourseGraph:
    graph = CourseGraph()
    graph.add_prerequisite("Programming Fundamentals", "Data Structures")
    graph.add_prerequisite("Data Structures", "Algorithms")
    graph.add_prerequisite("Discrete Mathematics", "Algorithms")
    graph.add_prerequisite("Algorithms", "Advanced Algorithms")
    return graph
