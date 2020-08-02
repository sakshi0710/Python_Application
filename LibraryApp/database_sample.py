import sqlite3

def create_table():
    con=sqlite3.connect("lite.db")
    cur= con.cursor()
    cur.execute("create table IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    
    con.commit()
    con.close()

def insert_into(item, quantity, price):
    con=sqlite3.connect("lite.db")
    cur= con.cursor()
    cur.execute("insert into store values (?,?,?)",( item, quantity, price))
    con.commit()
    con.close()



insert_into("wood", 12, 14.2)


def view_table():
    con=sqlite3.connect("lite.db")
    cur= con.cursor()
    cur.execute("select * from store")
    rows= cur.fetchall()
    con.close()
    return rows


print(view_table())
