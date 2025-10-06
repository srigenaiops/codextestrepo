class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = 'pending'  # status can be 'pending' or 'completed'

    def mark_completed(self):
        self.status = 'completed'

    def get_details(self):
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'status': self.status
        }