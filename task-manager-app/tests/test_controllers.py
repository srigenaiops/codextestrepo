import unittest
from src.controllers.task_controller import TaskController
from src.models.task import Task
from src.models.user import User

class TestTaskController(unittest.TestCase):

    def setUp(self):
        self.controller = TaskController()
        self.user = User(username="test_user")
        self.task = Task(title="Test Task", description="This is a test task", due_date="2023-10-01")

    def test_add_task(self):
        self.controller.add_task(self.user, self.task)
        self.assertIn(self.task, self.user.tasks)

    def test_complete_task(self):
        self.controller.add_task(self.user, self.task)
        self.controller.complete_task(self.user, self.task)
        self.assertTrue(self.task.status)

    def test_remove_task(self):
        self.controller.add_task(self.user, self.task)
        self.controller.remove_task(self.user, self.task)
        self.assertNotIn(self.task, self.user.tasks)

    def test_get_user_tasks(self):
        self.controller.add_task(self.user, self.task)
        tasks = self.controller.get_user_tasks(self.user)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], self.task)

if __name__ == '__main__':
    unittest.main()