import sqlite3


connection = sqlite3.connect("dibi.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        description TEXT,
                        price TEXT NOT NULL
                )
            ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        email TEXT NOT NULL,
        username TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance TEXT NOT NULL 
    )
    ''')
    connection.commit()


def add_user(username, email, age):
        cursor.execute("INSERT INTO Users(email, username, age, balance)"
                       " VALUES (?, ?, ?, 1000)", (f'{email}', f'{username}', f'{age}'))
        connection.commit()

def is_included(username):
        cursor.execute('SELECT * FROM Users')
        out = cursor.fetchall()
        for i in out:
            if username == i[2]:
                return True
        return False


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()


cursor.execute("DELETE FROM Products")
for num in range(1, 5):
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
               (f"Продукт {num}", f"Описание {num}", num * 100))
connection.commit()
