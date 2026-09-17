import unittest

from campusflow.course_graph import CourseGraph


class CourseGraphTests(unittest.TestCase):
    def test_topological_order_respects_prerequisite(self):
        graph = CourseGraph()
        graph.add_prerequisite("A", "B")
        graph.add_prerequisite("B", "C")
        order = graph.topological_order()
        self.assertLess(order.index("A"), order.index("B"))
        self.assertLess(order.index("B"), order.index("C"))

    def test_cycle_detection(self):
        graph = CourseGraph()
        graph.add_prerequisite("A", "B")
        graph.add_prerequisite("B", "A")
        with self.assertRaises(ValueError):
            graph.topological_order()

    def test_bfs_path(self):
        graph = CourseGraph()
        graph.add_prerequisite("A", "B")
        graph.add_prerequisite("B", "C")
        self.assertEqual(graph.find_path("A", "C"), ["A", "B", "C"])


if __name__ == "__main__":
    unittest.main()
