class Task:
  id_counter = 1

  def __init__(self, title, assigned_to):
    self.id = Task.id_counter
    Task.id_counter += 1
    self.title = title
    self.status = "incomplete"
    self.assigned_to = assigned_to

  def mark_complete(self):
    self.status = "complete"

  def __str__(self):
    return f"{self.id}: {self.title} [{self.status}] (Assigned to: {self.assigned_to})"