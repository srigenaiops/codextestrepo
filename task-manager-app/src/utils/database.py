import sqlite3

def connect_db(db_name='tasks.db'):
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            status TEXT NOT NULL DEFAULT 'pending'
        )
    ''')
    conn.commit()

def add_task(conn, title, description, due_date):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (title, description, due_date)
        VALUES (?, ?, ?)
    ''', (title, description, due_date))
    conn.commit()

def get_tasks(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    return cursor.fetchall()

def update_task_status(conn, task_id, status):
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tasks
        SET status = ?
        WHERE id = ?
    ''', (status, task_id))
    conn.commit()

def delete_task(conn, task_id):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()

def close_db(conn):
    conn.close()