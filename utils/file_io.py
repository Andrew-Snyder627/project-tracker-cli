import json
import os
from models.user import User
from models.project import Project
from models.task import Task

def load_data(filepath):
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r") as f:
            contents = f.read().strip()
            return json.loads(contents) if contents else []
    except json.JSONDecodeError:
        return []

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

# USERS
def serialize_users(users):
    return [
        {"id": u.id, "name": u.name, "email": u.email}
        for u in users
    ]

def deserialize_users(data):
    users = []
    for u in data:
        user = User(u["name"], u["email"])
        user.id = u["id"]
        users.append(user)
    return users

# PROJECTS
def serialize_projects(projects):
    return [
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "due_date": p.due_date,
            "user_id": p.user_id
        }
        for p in projects
    ]

def deserialize_projects(data):
    projects = []
    for p in data:
        project = Project(p["title"], p["description"], p["due_date"], p["user_id"])
        project.id = p["id"]
        projects.append(project)
    return projects

# TASKS
def serialize_tasks(tasks):
    return [
        {
            "id": t.id,
            "title": t.title,
            "status": t.status,
            "assigned_to": t.assigned_to
        }
        for t in tasks
    ]

def deserialize_tasks(data):
    tasks = []
    for t in data:
        task = Task(t["title"], t["assigned_to"])
        task.id = t["id"]
        task.status = t["status"]
        tasks.append(task)
    return tasks