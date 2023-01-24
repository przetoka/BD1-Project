import psycopg2

conn = psycopg2.connect(database="u0przetocka",
                        host="127.0.0.1",
                        user="u0przetocka",
                        password="0przetocka")

cursor = conn.cursor()

def login(email, password):
    cursor.execute("SELECT * FROM sklep.pracownik WHERE email = %s AND haslo = %s", [email, password])

    return cursor.fetchall()

def employees():
    cursor.execute("SELECT id_pracownik, imie, nazwisko, id_sklep, id_magazyn, nr_telefonu, email, rola FROM sklep.pracownik")

    return cursor.fetchall()

def warehouse_employees():
    cursor.execute("SELECT * FROM pracownicy_magazynow")

    return cursor.fetchall()

def shop_employees():
    cursor.execute("SELECT * FROM pracownicy_sklepow")

    return cursor.fetchall()

def insert(values):
    try:
        cursor.execute("INSERT INTO sklep.pracownik VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", values)
        conn.commit()
    except:
        cursor.execute("ROLLBACK")
        conn.commit()