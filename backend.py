import sqlite3

def connect():
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,titlu TEXT,autor TEXT,an_lansare INTEGER,editura TEXT)")
        conn.commit()
        conn.close()


def insert(title,autor,an_lansare,editura):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,autor,an_lansare,editura))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(titlu):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute('SELECT * FROM book WHERE titlu=?',(titlu,))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute('DELETE FROM book WHERE id=?',(id,))
    conn.commit()
    conn.close()


def update(id,newtitlu,newautor,newan,neweditura):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute('UPDATE book SET titlu=?, autor=?, an_lansare=?, editura=? WHERE id=?',(newtitlu,newautor,newan,neweditura,id))
    conn.commit()
    conn.close()    

connect()

print(view())
print("Cautare:")
print(search("IOn"))
update(1,"Ionisor","Crengulescu",1920,"UPT")
print(view())


