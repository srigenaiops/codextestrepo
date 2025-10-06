from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                           QPushButton, QListWidget, QInputDialog)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager")
        self.setGeometry(100, 100, 600, 400)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        self.task_list = QListWidget()
        layout.addWidget(self.task_list)
        
        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.add_task)
        layout.addWidget(add_button)
        
        complete_button = QPushButton("Mark Complete")
        complete_button.clicked.connect(self.mark_complete)
        layout.addWidget(complete_button)
        
    def add_task(self):
        task, ok = QInputDialog.getText(self, "Add Task", "Enter task:")
        if ok and task:
            self.task_list.addItem(task)
            
    def mark_complete(self):
        current_item = self.task_list.currentItem()
        if current_item:
            current_item.setText(f"✓ {current_item.text()}")