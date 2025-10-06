# README.md

# Task Manager App

## Overview
The Task Manager App is a Python-based user interface application designed to help users manage their daily tasks, personal work, learning, todos, and reminders. The application allows users to track ongoing tasks, highlight previously pending tasks, add new tasks, and mark completed tasks.

## Features
- Add new tasks with titles and descriptions
- Mark tasks as completed
- View a list of ongoing and pending tasks
- User-friendly interface for easy navigation

## Project Structure
```
task-manager-app
├── src
│   ├── main.py
│   ├── models
│   │   ├── task.py
│   │   └── user.py
│   ├── views
│   │   ├── main_window.py
│   │   ├── task_list.py
│   │   └── task_form.py
│   ├── controllers
│   │   └── task_controller.py
│   ├── utils
│   │   ├── database.py
│   │   └── date_helper.py
│   └── assets
│       └── styles.css
├── tests
│   ├── test_models.py
│   └── test_controllers.py
├── requirements.txt
├── setup.py
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd task-manager-app
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
python src/main.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you'd like to add.

## License
This project is licensed under the MIT License. See the LICENSE file for details.