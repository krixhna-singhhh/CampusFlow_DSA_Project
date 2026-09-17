# Project Statement - CampusFlow

## Problem Statement
Students often manage deadlines, prerequisite-heavy subjects, and study resources in separate places. This makes it harder to decide what to do first, understand course dependency order, and quickly locate useful study material. CampusFlow solves this through a command-line academic planner built around core Data Structures and Algorithms concepts.

## Scope
CampusFlow focuses on three academic planning tasks:
1. Task scheduling and progress tracking.
2. Course-prerequisite planning.
3. Study-resource cataloguing and searching.

The project is intentionally terminal-based so it can be executed in a minimal environment without a GUI.

## Target Users
- College students managing multiple subjects and deadlines.
- Learners who want a simple prerequisite map for courses.
- Students maintaining a local index of notes, worksheets and references.

## High-Level Features
- Add, list, complete and delete academic tasks.
- Heap-based recommendation of task execution order.
- Directed graph representation of course prerequisites.
- Topological sorting with cycle detection.
- BFS path discovery between prerequisite-linked courses.
- Add, list, search and delete study resources.
- Sorted resource list with prefix search and hash-based ID lookup.
- Terminal analytics for task subjects and resource types.
- JSON persistence, validation and automated unit tests.
