# CampusFlow - DSA-Based Academic Task and Course Planner

CampusFlow is a command-line project that applies core **Data Structures and Algorithms** to everyday academic planning. It combines task prioritization, course prerequisite planning, study-resource search, and simple analytics in one terminal application.

## 1. Main Features

### Module A - Task Manager and Priority Scheduler
- Add, list, complete, and delete tasks.
- Store priority, deadline, subject, and estimated work time.
- Recommend an execution order using a **binary heap / priority queue**.
- Show completion and pending-work statistics.

### Module B - Course Prerequisite Graph
- Represent prerequisites as a **directed graph**.
- Generate a valid study sequence using **topological sorting**.
- Detect invalid cyclic prerequisites.
- Find a prerequisite path using **breadth-first search (BFS)**.

### Module C - Study Resource Catalogue
- Add, list, search, and delete resources.
- Maintain resources in title-sorted order.
- Locate a title-prefix starting point using **binary search (`bisect`)**.
- Use a **hash table (`dict`)** for fast resource lookup by ID.
- Provide linear topic search for comparison.

### Analytics
- Count task distribution by subject.
- Count resource distribution by type.
- Render terminal-friendly ASCII bar charts.

## 2. Technologies Used

- Python 3.10 or newer
- Python standard library only
- JSON file storage
- `unittest` for automated tests
- Git/GitHub for version control
- Graphviz-generated design diagrams are already included as PNG files; Graphviz is **not required** to run the application.

## 3. Repository Structure

```text
CampusFlow_DSA_Project/
├── campusflow/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── models.py
│   ├── validators.py
│   ├── storage.py
│   ├── task_manager.py
│   ├── course_graph.py
│   ├── resource_catalog.py
│   ├── analytics.py
│   └── sample_data.py
├── tests/
│   ├── test_task_manager.py
│   ├── test_course_graph.py
│   ├── test_resource_catalog.py
│   └── test_analytics.py
├── config/settings.json
├── data/
│   ├── tasks.json
│   └── resources.json
├── docs/
│   ├── ALGORITHMS.md
│   ├── TESTING.md
│   ├── diagrams/
│   └── screenshots/
├── PROJECT_REPORT.pdf
├── README.md
├── statement.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

## 4. Environment Setup

### Step 1 - Install Python
Install **Python 3.10+** and verify it from a terminal:

```bash
python --version
```

On some macOS/Linux systems, use:

```bash
python3 --version
```

### Step 2 - Download or clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

If you downloaded the ZIP, extract it and open a terminal inside the extracted repository folder.

### Step 3 - Create a virtual environment (recommended)

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 4 - Install dependencies
CampusFlow has no third-party runtime dependencies, but the following command is safe and keeps setup consistent:

```bash
python -m pip install -r requirements.txt
```

### Step 5 - Configuration
No secret keys or external services are required. Default settings are stored in:

```text
config/settings.json
```

Application data is stored locally in:

```text
data/tasks.json
data/resources.json
```

## 5. Run the Project

All commands below must be run from the repository root.

### Load sample data

```bash
python -m campusflow seed
```

### View help

```bash
python -m campusflow --help
```

### Task commands

Add a task:

```bash
python -m campusflow task-add --title "Practice Trees" --subject "DSA" --priority 5 --deadline 2026-09-25 --hours 2
```

List tasks:

```bash
python -m campusflow task-list
```

Show only pending tasks:

```bash
python -m campusflow task-list --pending-only
```

Show recommended heap-based plan:

```bash
python -m campusflow task-plan
```

Show task statistics:

```bash
python -m campusflow task-stats
```

Complete or delete a task using the ID displayed by `task-list`:

```bash
python -m campusflow task-complete TASK_ID
python -m campusflow task-delete TASK_ID
```

### Course graph commands

Show a valid prerequisite order:

```bash
python -m campusflow course-plan
```

Find a BFS prerequisite path:

```bash
python -m campusflow course-path "Programming Fundamentals" "Advanced Algorithms"
```

### Resource commands

Add a resource:

```bash
python -m campusflow resource-add --title "AVL Tree Notes" --topic "balanced binary search tree" --type "Notes" --location "local/avl-notes.pdf"
```

List resources:

```bash
python -m campusflow resource-list
```

Search by title prefix:

```bash
python -m campusflow resource-search "Gra"
```

Search by topic text:

```bash
python -m campusflow resource-topic "heap"
```

Delete by ID:

```bash
python -m campusflow resource-delete RESOURCE_ID
```

### Analytics

```bash
python -m campusflow analytics
```

## 6. Testing Instructions

Run the complete automated test suite from the repository root:

```bash
python -m unittest discover -s tests -v
```

Expected result: all tests should finish with `OK`.

A quick manual smoke test is:

```bash
python -m campusflow seed
python -m campusflow task-list
python -m campusflow task-plan
python -m campusflow course-plan
python -m campusflow analytics
```

## 7. DSA Concepts Demonstrated

| Concept | Application in CampusFlow |
|---|---|
| Heap / Priority Queue | Scheduling pending tasks by priority and deadline |
| Directed Graph | Modelling prerequisite relationships |
| Topological Sort | Producing a valid course-learning sequence |
| BFS | Finding a path through prerequisite relationships |
| Hash Table | Resource lookup by unique ID |
| Binary Search | Finding the start of a title prefix in sorted data |
| Linear Search | Topic-text resource search |
| Sorting | Stable task/resource presentation |
| Counting / Hashing | Analytics summaries |

See `docs/ALGORITHMS.md` for complexity notes.

## 8. Design Documentation

The `docs/diagrams/` folder contains:
- System Architecture Diagram
- Workflow Diagram
- Use Case Diagram
- Class/Component Diagram
- Sequence Diagram

Both source `.dot` files and ready-to-view `.png` files are included.

## 9. Error Handling

CampusFlow validates:
- Empty text inputs
- Task priority range (1-5)
- Deadline format (`YYYY-MM-DD`)
- Positive estimated hours
- Self-dependency in course prerequisites
- Cycles in prerequisite graphs
- Missing task/resource IDs
- Missing/corrupted JSON data (safe defaults are used)

## 10. Resetting Local Data

To return the project to an empty state, replace the two data files with:

`data/tasks.json`

```json
{"tasks": []}
```

`data/resources.json`

```json
{"resources": []}
```

Then run `python -m campusflow seed` again if sample records are required.

## 11. Author

**Krishnapal Rajput**  
Registration No.: **25MIM10084**
