import tempfile
import unittest
from pathlib import Path

from campusflow.storage import JSONStorage
from campusflow.task_manager import TaskManager


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.manager = TaskManager(JSONStorage(str(Path(self.temp.name) / "tasks.json")))

    def tearDown(self):
        self.temp.cleanup()

    def test_add_and_complete_task(self):
        task = self.manager.add_task("Graphs", "DSA", 5, "2026-10-01", 2.0)
        self.assertEqual(len(self.manager.list_tasks()), 1)
        self.assertTrue(self.manager.complete_task(task.task_id))
        self.assertTrue(self.manager.get_task(task.task_id).completed)

    def test_priority_order(self):
        low = self.manager.add_task("Low", "DSA", 2, "2026-09-18", 1)
        high = self.manager.add_task("High", "DSA", 5, "2026-09-30", 1)
        order = self.manager.recommended_order()
        self.assertEqual(order[0].task_id, high.task_id)
        self.assertEqual(order[1].task_id, low.task_id)

    def test_invalid_priority(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("Bad", "DSA", 8, "2026-09-18", 1)


if __name__ == "__main__":
    unittest.main()
