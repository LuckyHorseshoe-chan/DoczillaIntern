import sqlite3

con = sqlite3.connect('todo.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE tasks
             (id string PRIMARY KEY, name text, shortDesc text, fullDesc text,
              date date, status bool)''')

# Insert rows of data
tasks_list = [
   ('cool_id','Сделать химию','Сделать химию Сделать химию','Сделать химию Сделать химию Сделать химию','22-05-2022', 1),
   ('nice_id', 'Сходить в магазин', 'Купить мясо, хлеб, яйца, молоко.', 'Купить мясо, хлеб, яйца, молоко. Сходить в Пятёрочку, Перекрёсток, Зельгрос, Метро или Глобус', '11-04-2022', 0),
   ('great_id', 'Съездить на дачу', 'Съездить на дачу Съездить на дачу', 'Съездить на дачу Съездить на дачу Съездить на дачу', '23-05-2022', 1),
   ('beautiful_id', 'Встретиться с Катей', 'Встретиться с Катей Встретиться с Катей', 'Встретиться с Катей Встретиться с Катей Встретиться с Катей', '26-05-2022', 1),
   ('smart_id', 'Сделать лабы по физике', 'Сделать лабы по физике Сделать лабы по физике', 'Сделать лабы по физике Сделать лабы по физике Сделать лабы по физике', '20-05-2022', 1),
   ('clever_id', 'Сдать курсач', 'Сдать курсач Сдать курсач', 'Сдать курсач Сдать курсач Сдать курсач', '22-05-2022', 1),
]
cur.executemany("INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?)", tasks_list)
# Save (commit) the changes
con.commit()
# Show results
for row in cur.execute('SELECT * FROM tasks'):
        print(row)
con.close()