class TaskForm:
    def __init__(self):
        self.title = ""
        self.description = ""
        self.due_date = None
        self.status = "Pending"

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def set_due_date(self, due_date):
        self.due_date = due_date

    def save_task(self):
        # Logic to save the task would go here
        pass

    def clear_form(self):
        self.title = ""
        self.description = ""
        self.due_date = None
        self.status = "Pending"