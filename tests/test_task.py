import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.task import Task

def test_task_creation_and_completion():
    task = Task("Write tests", "Alice")
    assert task.title == "Write tests"
    assert task.status == "incomplete"
    task.mark_complete()
    assert task.status == "complete"