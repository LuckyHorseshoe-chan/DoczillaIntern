import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('mydb.db')
    conn.row_factory = sqlite3.Row
    return conn
def get_student(student_id):
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE Идентификатор = ?',
                        (student_id,)).fetchone()
    conn.close()
    if student is None:
        abort(404)
    return student

@app.route('/')
def index():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('base.html', title='Students', students=students)
@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        student_id = request.form['id']
        name = request.form['name']
        surname = request.form['surname']
        patronym = request.form['patronym']
        date = request.form['date']
        group = request.form['group']

        if not student_id:
            flash('Id is required!')
        elif not name:
            flash('Name is required!')
        elif not surname:
            flash('Surname is required!')
        elif not patronym:
            flash('Patronym is required!')
        elif not date:
            flash('Date is required!')
        elif not group:
            flash('Group is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO students VALUES (?, ?, ?, ?, ?, ?)',
                         (student_id, name, surname, patronym, date, group))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')
@app.route('/delete/', methods=('POST', 'GET'))
def delete():
    if request.method == 'POST':
        student_id = request.form['id']
        student = get_student(student_id)
        conn = get_db_connection()
        conn.execute('DELETE FROM students WHERE Идентификатор = ?', (student_id,))
        conn.commit()
        conn.close()
        flash('"{0} {1}" отчислен(а)!'.format(student['Имя'], student['Фамилия']))
        return redirect(url_for('index'))
    return render_template('delete.html')