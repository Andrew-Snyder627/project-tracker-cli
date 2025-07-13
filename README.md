# 📋 Project Tracker CLI

A command-line project management tool built in Python. Allows you to manage users, projects, and tasks — all stored persistently in JSON files.

---

## 🚀 Features

- Add and list users
- Add projects to users
- Assign tasks to projects
- Mark tasks as complete
- List all projects and tasks
- Pretty CLI output using `rich`
- Persistent local data storage (JSON)

---

## 🛠 Setup Instructions

1. Clone the repo:

   ```
   git clone https://github.com/YOUR_USERNAME/project_tracker_cli.git
   cd project_tracker_cli
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

---

## 🧪 Running the CLI

### Add a user

```bash
python main.py add-user --name "Alice" --email "alice@example.com"
```

### Add a project

```bash
python main.py add-project --user "Alice" --title "CLI Tool" --description "Build a project tracker" --due-date "2025-08-01"
```

### Add a task

```bash
python main.py add-task --project "CLI Tool" --title "Write unit tests" --assigned-to "Bob"
```

### Complete a task

```bash
python main.py complete-task --task-id 1
```

### List all users

```bash
python main.py list-users
```

### List all projects (optionally by user)

```bash
python main.py list-projects
python main.py list-projects --user "Alice"
```

### List all tasks

```bash
python main.py list-tasks
```

---

## 🗂 Project Structure

```
project_tracker_cli/
├── data/              # JSON storage files
├── models/            # Class definitions (User, Project, Task)
├── utils/             # File I/O utilities
├── tests/             # Unit tests
├── main.py            # CLI entry point
├── requirements.txt
└── README.md
```

---

## ✅ Requirements

- Python 3.10+
- [rich](https://pypi.org/project/rich/) (for styled CLI output)

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🧪 Running Tests

```bash
pytest
```

Tests are located in the `tests/` folder and cover each major model.

---
