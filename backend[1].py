import sqlite3


def connect():
    conn = sqlite3.connect('agency.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS passengers(id INTEGER PRIMARY KEY,name text,phone text,destination INTEGER,age INTEGER)")
    conn.commit()
    conn.close()


def insert(name, phone, destination, age):
    conn = sqlite3.connect('agency.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO passengers VALUES (NULL,?,?,?,?)", (name, phone, destination, age))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('agency.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM passengers")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(name="", phone="", destination="", age=""):
    conn = sqlite3.connect('agency.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM passengers WHERE name=? or phone=? or destination=? or age=?", (name, phone, destination, age))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect('agency.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM passengers WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def update(ID, name, city, year, roomNo):
    conn = sqlite3.connect('agency.db')
    cur = conn.cursor()
    cur.execute("UPDATE passengers SET name=?, phone=?, destination=?, age=? WHERE id=?", (name, phone, destination, age,id))
    conn.commit()
    conn.close()


connect()
# insert("ghazal", "Italy", 09555555555, 25)
# insert("Sanaz", "France", 09666666666, 14)
# insert("Mohammad", "Germany", 09777777777, 34)
# insert("Maryam", "Austria", 09888888888, 54)


# delete(9)
# update(3,"Alireza","Milano",1345,43)
# print(view())
