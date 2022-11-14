import random
import sqlite3
#
# conn = sqlite3.connect('hw.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(menu int)''')
# conn.commit()
# num = int(input("Num: "))
# cursor.execute('''INSERT INTO tab_1(menu) VALUES (?)''' ,(num,))
# conn.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# k = cursor.fetchall()
# print(k)
#
# cursor.execute('''''')
conn = sqlite3.connect('sun.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT, col_2 INT)''')

for i in range(3):
    num = random.randint(1, 9)
    num_1 = random.randint(1, 9)
    cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?,?)''' ,(num, num_1))
conn.commit()
cursor.execute('''SELECT id FROM tab_1''')
k = cursor.fetchall()
# print(*k)

r = random.choice(k)
print(r)
cursor.execute('''SELECT col_1,col_2 FROM tab_1 WHERE id=?''' ,(r))
o = cursor.fetchall()
print(*o)
if o[0][0] % 2 == 0 and o[0][1] % 2 == 0:
    cursor.execute('''DELETE FROM tab_1 WHERE id=?''',(r))
else:
    cursor.execute('''UPDATE tab_1 SET col_1=2, col_2=2 WHERE id=?''' ,(r))
cursor.execute('''SELECT * FROM tab_1''')
o = cursor.fetchall()
print(*o)



