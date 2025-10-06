class TaskList:
    def __init__(self, tasks):
        self.tasks = tasks

    def display_tasks(self):
        for task in self.tasks:
            status = "✔️" if task.status == "completed" else "❌"
            print(f"{status} {task.title} - Due: {task.due_date}")

    def highlight_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if task.status != "completed"]
        for task in pending_tasks:
            print(f"🔴 Pending: {task.title} - Due: {task.due_date}")