import unittest
from src.models.task import Task
from src.models.user import User

class TestTask(unittest.TestCase):
    def setUp(self):
        self.task = Task(title="Test Task", description="This is a test task", due_date="2023-10-01")
    
    def test_task_creation(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "This is a test task")
        self.assertEqual(self.task.due_date, "2023-10-01")
        self.assertEqual(self.task.status, "pending")

    def test_mark_completed(self):
        self.task.mark_completed()
        self.assertEqual(self.task.status, "completed")

    def test_get_details(self):
        details = self.task.get_details()
        self.assertEqual(details['title'], "Test Task")
        self.assertEqual(details['description'], "This is a test task")
        self.assertEqual(details['due_date'], "2023-10-01")
        self.assertEqual(details['status'], "pending")

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(username="testuser")
        self.task1 = Task(title="Task 1", description="First task", due_date="2023-10-01")
        self.task2 = Task(title="Task 2", description="Second task", due_date="2023-10-02")
        self.user.add_task(self.task1)
        self.user.add_task(self.task2)

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(len(self.user.tasks), 2)

    def test_add_task(self):
        task3 = Task(title="Task 3", description="Third task", due_date="2023-10-03")
        self.user.add_task(task3)
        self.assertEqual(len(self.user.tasks), 3)

    def test_remove_task(self):
        self.user.remove_task(self.task1)
        self.assertEqual(len(self.user.tasks), 1)
        self.assertNotIn(self.task1, self.user.tasks)

if __name__ == '__main__':
    unittest.main()