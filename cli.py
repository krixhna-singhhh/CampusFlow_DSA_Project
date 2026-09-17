import argparse
from pathlib import Path

from .analytics import ascii_bar_chart, resource_type_distribution, task_subject_distribution
from .resource_catalog import ResourceCatalog
from .sample_data import build_sample_course_graph, seed_if_empty
from .storage import JSONStorage
from .task_manager import TaskManager


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"


def managers():
    task_manager = TaskManager(JSONStorage(str(DATA_DIR / "tasks.json")))
    catalog = ResourceCatalog(JSONStorage(str(DATA_DIR / "resources.json")))
    return task_manager, catalog


def print_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "DONE" if task.completed else "PENDING"
        print(f"{task.task_id} | {status:<7} | P{task.priority} | {task.deadline} | {task.subject} | {task.title} | {task.estimated_hours}h")


def print_resources(resources):
    if not resources:
        print("No resources found.")
        return
    for resource in resources:
        print(f"{resource.resource_id} | {resource.title} | {resource.topic} | {resource.resource_type} | {resource.location}")


def build_parser():
    parser = argparse.ArgumentParser(
        prog="campusflow",
        description="CampusFlow: a command-line DSA-based academic task and course planner.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("seed", help="Load sample data if data files are empty.")

    task_add = sub.add_parser("task-add", help="Add a task.")
    task_add.add_argument("--title", required=True)
    task_add.add_argument("--subject", required=True)
    task_add.add_argument("--priority", required=True, type=int)
    task_add.add_argument("--deadline", required=True)
    task_add.add_argument("--hours", required=True, type=float)

    task_list = sub.add_parser("task-list", help="List tasks.")
    task_list.add_argument("--pending-only", action="store_true")

    task_complete = sub.add_parser("task-complete", help="Mark a task complete.")
    task_complete.add_argument("task_id")

    task_delete = sub.add_parser("task-delete", help="Delete a task.")
    task_delete.add_argument("task_id")

    sub.add_parser("task-plan", help="Show heap-based recommended task order.")
    sub.add_parser("task-stats", help="Show task statistics.")

    res_add = sub.add_parser("resource-add", help="Add a study resource.")
    res_add.add_argument("--title", required=True)
    res_add.add_argument("--topic", required=True)
    res_add.add_argument("--type", required=True, dest="resource_type")
    res_add.add_argument("--location", required=True)

    sub.add_parser("resource-list", help="List all resources.")

    res_search = sub.add_parser("resource-search", help="Search resources by title prefix.")
    res_search.add_argument("prefix")

    res_topic = sub.add_parser("resource-topic", help="Linear-search resources by topic text.")
    res_topic.add_argument("topic")

    res_delete = sub.add_parser("resource-delete", help="Delete a resource.")
    res_delete.add_argument("resource_id")

    sub.add_parser("course-plan", help="Show topological course order.")
    path = sub.add_parser("course-path", help="Find a BFS prerequisite path in sample graph.")
    path.add_argument("start")
    path.add_argument("target")

    sub.add_parser("analytics", help="Display ASCII analytics charts.")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    task_manager, catalog = managers()

    try:
        if args.command == "seed":
            seed_if_empty(task_manager, catalog)
            print("Sample data is ready.")
        elif args.command == "task-add":
            task = task_manager.add_task(args.title, args.subject, args.priority, args.deadline, args.hours)
            print(f"Task added: {task.task_id}")
        elif args.command == "task-list":
            print_tasks(task_manager.list_tasks(include_completed=not args.pending_only))
        elif args.command == "task-complete":
            print("Task completed." if task_manager.complete_task(args.task_id) else "Task ID not found.")
        elif args.command == "task-delete":
            print("Task deleted." if task_manager.delete_task(args.task_id) else "Task ID not found.")
        elif args.command == "task-plan":
            print_tasks(task_manager.recommended_order())
        elif args.command == "task-stats":
            stats = task_manager.stats()
            for key, value in stats.items():
                print(f"{key}: {value}")
        elif args.command == "resource-add":
            resource = catalog.add(args.title, args.topic, args.resource_type, args.location)
            print(f"Resource added: {resource.resource_id}")
        elif args.command == "resource-list":
            print_resources(catalog.list_all())
        elif args.command == "resource-search":
            print_resources(catalog.search_title_prefix(args.prefix))
        elif args.command == "resource-topic":
            print_resources(catalog.search_topic_linear(args.topic))
        elif args.command == "resource-delete":
            print("Resource deleted." if catalog.delete(args.resource_id) else "Resource ID not found.")
        elif args.command == "course-plan":
            graph = build_sample_course_graph()
            print(" -> ".join(graph.topological_order()))
        elif args.command == "course-path":
            graph = build_sample_course_graph()
            path = graph.find_path(args.start, args.target)
            print(" -> ".join(path) if path else "No path found.")
        elif args.command == "analytics":
            print("Task distribution by subject")
            print(ascii_bar_chart(task_subject_distribution(task_manager.tasks)))
            print("\nResource distribution by type")
            print(ascii_bar_chart(resource_type_distribution(catalog.resources)))
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
