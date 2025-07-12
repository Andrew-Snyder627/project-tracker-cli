class User:
  id_counter = 1

  def __init__(self, name, email):
    self.id = User.id_counter
    User.id_counter += 1
    self.name = name
    self.email = email
    self.projects = []

  def add_project(self, project):
    self.projects.append(project)

  def __str__(self):
    return f"{self.id}: {self.name} <{self.email}>"