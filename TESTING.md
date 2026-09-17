# Testing Notes

Run all automated tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

Covered cases include:
- Task creation and completion.
- Heap-based priority ordering.
- Rejection of invalid priority values.
- Topological ordering.
- Graph cycle detection.
- BFS path discovery.
- Resource title prefix search.
- Hash-based resource lookup.
- ASCII analytics output.

Manual smoke test:

```bash
python -m campusflow seed
python -m campusflow task-list
python -m campusflow task-plan
python -m campusflow course-plan
python -m campusflow analytics
```
