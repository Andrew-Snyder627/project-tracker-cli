class Project:
  id_counter = 1

  def __init__(self, title, description, due_date, user_id):
    self.id = Project.id_counter
    self.title = title
    self.description = description
    self.due_date = due_date
    self.user_id = user_id
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)

  def __str__(self):
    return f"{self.id}: {self.title} (Due: {self.due_date})"