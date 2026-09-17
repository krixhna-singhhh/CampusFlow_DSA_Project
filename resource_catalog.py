import bisect
import uuid
from typing import Dict, List, Optional

from .models import Resource
from .storage import JSONStorage
from .validators import non_empty


class ResourceCatalog:
    """Resource CRUD with hash index and binary-search title lookup."""

    def __init__(self, storage: JSONStorage):
        self.storage = storage
        self.resources: List[Resource] = []
        self.by_id: Dict[str, Resource] = {}
        self._load()

    def _load(self) -> None:
        raw = self.storage.load({"resources": []})
        self.resources = [Resource.from_dict(item) for item in raw.get("resources", [])]
        self._reindex()

    def _persist(self) -> None:
        self.storage.save({"resources": [resource.to_dict() for resource in self.resources]})

    def _reindex(self) -> None:
        self.resources.sort(key=lambda item: item.title.lower())
        self.by_id = {resource.resource_id: resource for resource in self.resources}

    def add(self, title: str, topic: str, resource_type: str, location: str) -> Resource:
        resource = Resource(
            resource_id=str(uuid.uuid4())[:8],
            title=non_empty(title, "Title"),
            topic=non_empty(topic, "Topic"),
            resource_type=non_empty(resource_type, "Resource type"),
            location=non_empty(location, "Location"),
        )
        self.resources.append(resource)
        self._reindex()
        self._persist()
        return resource

    def list_all(self) -> List[Resource]:
        return list(self.resources)

    def get_by_id(self, resource_id: str) -> Optional[Resource]:
        return self.by_id.get(resource_id)

    def delete(self, resource_id: str) -> bool:
        if resource_id not in self.by_id:
            return False
        self.resources = [r for r in self.resources if r.resource_id != resource_id]
        self._reindex()
        self._persist()
        return True

    def search_title_prefix(self, prefix: str) -> List[Resource]:
        prefix = prefix.strip().lower()
        if not prefix:
            return []
        titles = [resource.title.lower() for resource in self.resources]
        start = bisect.bisect_left(titles, prefix)
        result = []
        for idx in range(start, len(self.resources)):
            if titles[idx].startswith(prefix):
                result.append(self.resources[idx])
            else:
                break
        return result

    def search_topic_linear(self, topic: str) -> List[Resource]:
        key = topic.strip().lower()
        return [resource for resource in self.resources if key in resource.topic.lower()]
