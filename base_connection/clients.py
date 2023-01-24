import psycopg2

conn = psycopg2.connect(database="u0przetocka",
                        host="127.0.0.1",
                        user="u0przetocka",
                        password="0przetocka")
cursor = conn.cursor()

def clients():
    cursor.execute("SELECT * FROM sklep.klient")

    return cursor.fetchall()
    
def clients_order():
    cursor.execute("SELECT id_klient, imie, nazwisko FROM sklep.klient")

    return cursor.fetchall()

def insert(values):
    try:
        cursor.execute("INSERT INTO sklep.klient VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", values)
        conn.commit()
    except:
        cursor.execute("ROLLBACK")
        conn.commit()
