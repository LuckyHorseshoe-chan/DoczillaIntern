import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    return conn
def get_task(task_id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE Идентификатор = ?',
                        (task_id,)).fetchone()
    conn.close()
    if task is None:
        abort(404)
    return task

@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)