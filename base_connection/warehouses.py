import psycopg2

conn = psycopg2.connect(database="u0przetocka",
                        host="127.0.0.1",
                        user="u0przetocka",
                        password="0przetocka")

cursor = conn.cursor()
def warehouses():
    cursor.execute("SELECT * FROM sklep.magazyn")
    
    return cursor.fetchall()

def insert(values):
    try:
        cursor.execute("INSERT INTO sklep.magazyn VALUES(%s, %s, %s, %s, %s, %s)", values)
        conn.commit()
    except:
        cursor.execute("ROLLBACK")
        conn.commit()


def add_item(values):
    try:
        cursor.execute("INSERT INTO sklep.produkty_na_stanie(id_magazyn, id_produkt, ilosc) VALUES(%s, %s, %s)", values)
        conn.commit()
    except:
        cursor.execute("ROLLBACK")
        conn.commit()

conn.close()