import sqlite3

conn = sqlite3.connect('orfDB.db')
c = conn.cursor()
#c.execute('''CREATE TABLE dictionary
#        (id integer, name text)''')

#Удаление элемента по его айди(если айди повторяется, то все элементы с этим айди будут удалены)
#conn.execute("DELETE from dict where name='';")
#conn.execute("DELETE FROM dict2")
f = open('orf_2.txt')
i = 1
str = []
k=0
for line in f:
    ln = []
    ln.append(i)
    ln.append(line)
    i += 1
    str.append(ln)
    c.executemany('INSERT INTO dictionary VALUES ( ?, ?)', str)
    str = []
conn.commit()
conn.close()