from collections import defaultdict, deque
from typing import Dict, List, Set, Tuple


class CourseGraph:
    """Directed graph for course prerequisite relationships."""

    def __init__(self):
        self.graph: Dict[str, Set[str]] = defaultdict(set)
        self.nodes: Set[str] = set()

    def add_course(self, course: str) -> None:
        course = course.strip()
        if not course:
            raise ValueError("Course name cannot be empty.")
        self.nodes.add(course)
        self.graph.setdefault(course, set())

    def add_prerequisite(self, prerequisite: str, course: str) -> None:
        prerequisite = prerequisite.strip()
        course = course.strip()
        if not prerequisite or not course:
            raise ValueError("Course names cannot be empty.")
        if prerequisite == course:
            raise ValueError("A course cannot be its own prerequisite.")
        self.add_course(prerequisite)
        self.add_course(course)
        self.graph[prerequisite].add(course)

    def topological_order(self) -> List[str]:
        indegree = {node: 0 for node in self.nodes}
        for src in self.nodes:
            for dst in self.graph[src]:
                indegree[dst] += 1

        queue = deque(sorted(node for node, degree in indegree.items() if degree == 0))
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in sorted(self.graph[node]):
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != len(self.nodes):
            raise ValueError("Cycle detected: prerequisite plan is invalid.")
        return order

    def find_path(self, start: str, target: str) -> List[str]:
        if start not in self.nodes or target not in self.nodes:
            return []
        queue = deque([(start, [start])])
        visited = {start}
        while queue:
            node, path = queue.popleft()
            if node == target:
                return path
            for neighbor in sorted(self.graph[node]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return []

    def edges(self) -> List[Tuple[str, str]]:
        return sorted((src, dst) for src in self.nodes for dst in self.graph[src])
