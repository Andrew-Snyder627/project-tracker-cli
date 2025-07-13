import argparse
from models.user import User
from models.project import Project
from models.task import Task
from utils.file_io import (
    load_data, save_data,
    serialize_users, deserialize_users,
    serialize_projects, deserialize_projects,
    serialize_tasks, deserialize_tasks
)
from rich import print

# File paths
USER_FILE = "data/users.json"
PROJECT_FILE = "data/projects.json"
TASK_FILE = "data/tasks.json"

# Load data
users = deserialize_users(load_data(USER_FILE))
projects = deserialize_projects(load_data(PROJECT_FILE))
tasks = deserialize_tasks(load_data(TASK_FILE))


# COMMANDS

def add_user(args):
    user = User(args.name, args.email)
    users.append(user)
    save_data(USER_FILE, serialize_users(users))
    print(f"[green]User added:[/green] {user}")

def list_users(args):
    if not users:
        print("[yellow]No users found.[/yellow]")
    for u in users:
        print(u)

def add_project(args):
    user = next((u for u in users if u.name == args.user), None)
    if not user:
        print(f"[red]User '{args.user}' not found.[/red]")
        return
    project = Project(args.title, args.description, args.due_date, user.id)
    projects.append(project)
    save_data(PROJECT_FILE, serialize_projects(projects))
    print(f"[green]Project added:[/green] {project}")

def list_projects(args):
    if args.user:
        user = next((u for u in users if u.name == args.user), None)
        if not user:
            print(f"[red]User '{args.user}' not found.[/red]")
            return
        user_projects = [p for p in projects if p.user_id == user.id]
        for p in user_projects:
            print(p)
    else:
        for p in projects:
            print(p)

def add_task(args):
    project = next((p for p in projects if p.title == args.project), None)
    if not project:
        print(f"[red]Project '{args.project}' not found.[/red]")
        return
    task = Task(args.title, args.assigned_to)
    project.tasks.append(task)  # in-memory
    tasks.append(task)
    save_data(TASK_FILE, serialize_tasks(tasks))
    print(f"[green]Task added:[/green] {task}")

def list_tasks(args):
    for t in tasks:
        print(t)

def complete_task(args):
    task = next((t for t in tasks if t.id == args.task_id), None)
    if not task:
        print(f"[red]Task ID {args.task_id} not found.[/red]")
        return
    task.mark_complete()
    save_data(TASK_FILE, serialize_tasks(tasks))
    print(f"[green]Task marked complete:[/green] {task}")


# CLI SETUP

def setup_parser():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers()

    # Add user
    user_parser = subparsers.add_parser("add-user")
    user_parser.add_argument("--name", required=True)
    user_parser.add_argument("--email", required=True)
    user_parser.set_defaults(func=add_user)

    # List users
    list_users_parser = subparsers.add_parser("list-users")
    list_users_parser.set_defaults(func=list_users)

    # Add project
    proj_parser = subparsers.add_parser("add-project")
    proj_parser.add_argument("--user", required=True)
    proj_parser.add_argument("--title", required=True)
    proj_parser.add_argument("--description", required=True)
    proj_parser.add_argument("--due-date", required=True)
    proj_parser.set_defaults(func=add_project)

    # List projects
    list_proj_parser = subparsers.add_parser("list-projects")
    list_proj_parser.add_argument("--user")
    list_proj_parser.set_defaults(func=list_projects)

    # Add task
    task_parser = subparsers.add_parser("add-task")
    task_parser.add_argument("--project", required=True)
    task_parser.add_argument("--title", required=True)
    task_parser.add_argument("--assigned-to", required=True)
    task_parser.set_defaults(func=add_task)

    # List tasks
    list_task_parser = subparsers.add_parser("list-tasks")
    list_task_parser.set_defaults(func=list_tasks)

    # Complete task
    complete_task_parser = subparsers.add_parser("complete-task")
    complete_task_parser.add_argument("--task-id", required=True, type=int)
    complete_task_parser.set_defaults(func=complete_task)

    return parser


# MAIN

if __name__ == "__main__":
    parser = setup_parser()
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()