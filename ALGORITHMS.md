# Algorithms and Data Structures Used

| Feature | DSA concept | Main complexity |
|---|---|---|
| Recommended task order | Binary heap / priority queue | Build by pushes: O(n log n), each pop O(log n) |
| Course prerequisite model | Directed adjacency-list graph | O(V + E) storage/traversal |
| Valid course sequence | Kahn's topological sort | O(V + E) |
| Prerequisite path | Breadth-first search | O(V + E) |
| Resource ID lookup | Hash table (`dict`) | Average O(1) |
| Sorted resource catalogue | Ordered list | O(n log n) sort after mutation |
| Title prefix start position | Binary search (`bisect_left`) | O(log n) to locate start |
| Topic search | Linear search | O(n) |
| Analytics counting | Hash counting / Counter | O(n) |

## Why these choices
A heap matches task scheduling because only the next best task needs to be selected repeatedly. A directed graph naturally represents prerequisite relationships. Topological sorting gives a valid learning order, while BFS finds the shortest edge-count path in an unweighted prerequisite graph. For resources, a dictionary gives fast direct retrieval by ID, while maintaining titles in sorted order makes prefix lookup deterministic and efficient at locating the first possible match.
