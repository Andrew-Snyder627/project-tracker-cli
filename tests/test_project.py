import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.project import Project

def test_project_creation():
    project = Project("Build CLI", "Create CLI tool", "2025-08-01", user_id=1)
    assert project.title == "Build CLI"
    assert project.description == "Create CLI tool"
    assert project.due_date == "2025-08-01"
    assert project.user_id == 1
    assert project.tasks == []