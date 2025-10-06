class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks

    def __str__(self):
        return f'User: {self.username}, Tasks: {len(self.tasks)}'