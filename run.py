from app.model.task import Task

tasks = Task.select().get()

for task in tasks:
    print(task.name)

