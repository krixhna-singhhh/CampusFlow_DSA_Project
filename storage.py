import json
from pathlib import Path
from typing import Any, Dict


class JSONStorage:
    """Small JSON persistence layer with safe defaults and atomic-like overwrite."""

    def __init__(self, path: str):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self, default: Dict[str, Any]) -> Dict[str, Any]:
        if not self.path.exists():
            return default
        try:
            with self.path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
            return data if isinstance(data, dict) else default
        except (json.JSONDecodeError, OSError):
            return default

    def save(self, data: Dict[str, Any]) -> None:
        temp_path = self.path.with_suffix(self.path.suffix + ".tmp")
        with temp_path.open("w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2)
        temp_path.replace(self.path)
