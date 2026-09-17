import heapq
import uuid
from datetime import datetime
from typing import List, Optional

from .models import Task
from .storage import JSONStorage
from .validators import non_empty, validate_deadline, validate_positive_float, validate_priority


class TaskManager:
    """Task CRUD plus heap-based priority scheduling."""

    def __init__(self, storage: JSONStorage):
        self.storage = storage
        self.tasks: List[Task] = []
        self._load()

    def _load(self) -> None:
        raw = self.storage.load({"tasks": []})
        self.tasks = [Task.from_dict(item) for item in raw.get("tasks", [])]

    def _persist(self) -> None:
        self.storage.save({"tasks": [task.to_dict() for task in self.tasks]})

    def add_task(self, title: str, subject: str, priority: int, deadline: str, estimated_hours: float) -> Task:
        task = Task(
            task_id=str(uuid.uuid4())[:8],
            title=non_empty(title, "Title"),
            subject=non_empty(subject, "Subject"),
            priority=validate_priority(priority),
            deadline=validate_deadline(deadline),
            estimated_hours=validate_positive_float(estimated_hours, "Estimated hours"),
        )
        self.tasks.append(task)
        self._persist()
        return task

    def list_tasks(self, include_completed: bool = True) -> List[Task]:
        tasks = self.tasks if include_completed else [task for task in self.tasks if not task.completed]
        return sorted(tasks, key=lambda t: (t.completed, t.deadline, -t.priority, t.title.lower()))

    def get_task(self, task_id: str) -> Optional[Task]:
        return next((task for task in self.tasks if task.task_id == task_id), None)

    def complete_task(self, task_id: str) -> bool:
        task = self.get_task(task_id)
        if not task:
            return False
        task.completed = True
        self._persist()
        return True

    def delete_task(self, task_id: str) -> bool:
        before = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        changed = len(self.tasks) != before
        if changed:
            self._persist()
        return changed

    def recommended_order(self) -> List[Task]:
        """Return incomplete tasks using a heap: higher priority, then earlier deadline."""
        heap = []
        for task in self.tasks:
            if not task.completed:
                deadline_ord = datetime.strptime(task.deadline, "%Y-%m-%d").toordinal()
                heapq.heappush(heap, (-task.priority, deadline_ord, task.estimated_hours, task.task_id, task))
        ordered = []
        while heap:
            ordered.append(heapq.heappop(heap)[-1])
        return ordered

    def stats(self) -> dict:
        total = len(self.tasks)
        completed = sum(task.completed for task in self.tasks)
        pending = total - completed
        pending_hours = sum(task.estimated_hours for task in self.tasks if not task.completed)
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "pending_hours": round(pending_hours, 2),
        }
