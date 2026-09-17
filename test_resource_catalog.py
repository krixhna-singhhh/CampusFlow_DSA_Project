import tempfile
import unittest
from pathlib import Path

from campusflow.resource_catalog import ResourceCatalog
from campusflow.storage import JSONStorage


class ResourceCatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.catalog = ResourceCatalog(JSONStorage(str(Path(self.temp.name) / "resources.json")))

    def tearDown(self):
        self.temp.cleanup()

    def test_prefix_search(self):
        self.catalog.add("Graph Notes", "graphs", "Notes", "local")
        self.catalog.add("Heap Notes", "heaps", "Notes", "local")
        result = self.catalog.search_title_prefix("Gra")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "Graph Notes")

    def test_hash_lookup_by_id(self):
        resource = self.catalog.add("Sorting", "sorting", "Sheet", "local")
        self.assertEqual(self.catalog.get_by_id(resource.resource_id).title, "Sorting")


if __name__ == "__main__":
    unittest.main()
