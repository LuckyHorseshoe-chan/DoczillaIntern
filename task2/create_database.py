import sqlite3

con = sqlite3.connect('mydb.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE students
              (Идентификатор integer PRIMARY KEY, Имя text, Фамилия text, Отчество text,
              Дата_рождения date, Группа text)''')

# Insert rows of data
student_list = [
   (1,'Амелия','Иванова','Ивановна','23-04-2001','иу3_43б')
   (2, 'Лейла', 'Сергеева', 'Сергеевна', '11-01-2002', 'ибм1_31б'),
   (3, 'Елизавета', 'Андреева', 'Андреевна', '28-12-2000', 'фн_42б'),
   (4, 'Никита', 'Петров', 'Петрович', '26-05-2001', 'иу6_44б'),
   (5, 'Александр', 'Шварц', 'Романович', '05-07-2001', 'ла4_43б'),
   (6, 'Марк', 'Вайсс', 'Павлович', '12-04-2001', 'рт5_41б'),
]
cur.executemany("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?)", student_list)
# Save (commit) the changes
con.commit()
# Show results
for row in cur.execute('SELECT * FROM students'):
        print(row)
con.close()
