from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class Task:
    task_id: str
    title: str
    subject: str
    priority: int
    deadline: str
    estimated_hours: float
    completed: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        return cls(**data)


@dataclass
class Resource:
    resource_id: str
    title: str
    topic: str
    resource_type: str
    location: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Resource":
        return cls(**data)
