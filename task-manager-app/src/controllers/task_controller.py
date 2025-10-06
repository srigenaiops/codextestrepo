class TaskController:
    def __init__(self, task_model, user_model):
        self.task_model = task_model
        self.user_model = user_model

    def add_task(self, title, description, due_date):
        new_task = self.task_model(title, description, due_date)
        # Logic to save the new task to the database
        return new_task

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        task = self.get_task_by_id(task_id)
        if task:
            if title:
                task.title = title
            if description:
                task.description = description
            if due_date:
                task.due_date = due_date
            if status is not None:
                task.status = status
            # Logic to save the updated task to the database
            return task
        return None

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            # Logic to delete the task from the database
            return True
        return False

    def get_task_by_id(self, task_id):
        # Logic to retrieve a task by its ID from the database
        pass

    def get_all_tasks(self):
        # Logic to retrieve all tasks from the database
        pass

    def mark_task_completed(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task.status = 'completed'
            # Logic to save the updated task to the database
            return task
        return None