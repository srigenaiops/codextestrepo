from setuptools import setup, find_packages

setup(
    name='task-manager-app',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python-based UI application for managing daily work, personal tasks, and reminders.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'tkinter',  # or any other UI library you choose
        'sqlalchemy',  # if using SQLAlchemy for database interactions
        'pytest',  # for testing
    ],
    entry_points={
        'console_scripts': [
            'task-manager=main:main',  # Adjust according to your main function location
        ],
    },
)