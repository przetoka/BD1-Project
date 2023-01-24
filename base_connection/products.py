import psycopg2

conn = psycopg2.connect(database="u0przetocka",
                        host="127.0.0.1",
                        user="u0przetocka",
                        password="0przetocka")

cursor = conn.cursor()

def products():
    cursor.execute("SELECT * FROM sklep.produkt")
    
    return cursor.fetchall()

def products_in_warehouses():
    cursor.execute("SELECT * FROM produkty_w_magazynach")
    
    return cursor.fetchall()

def products_in_shops():
    cursor.execute("SELECT * FROM produkty_w_sklepach")
    
    return cursor.fetchall()

def insert(values):
    try:
        cursor.execute("INSERT INTO sklep.produkt VALUES(%s, %s, %s, %s, %s)", values)
        conn.commit()
    except:
        cursor.execute("ROLLBACK")
        conn.commit()