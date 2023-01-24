import psycopg2
from datetime import date
import base_connection.products as p

conn = psycopg2.connect(database="u0przetocka",
                        host="127.0.0.1",
                        user="u0przetocka",
                        password="0przetocka")

cursor = conn.cursor()

def orders():
    cursor.execute("SELECT * FROM sklep.zamowienie")
    
    return cursor.fetchall()

def orders_outline():
    cursor.execute("SELECT * FROM zamowienia_Zarys")
    
    return cursor.fetchall()

def orders_products():
    cursor.execute("SELECT * FROM zamowienia_produkty")
    
    return cursor.fetchall()

def orders_clients():
    cursor.execute("SELECT * FROM zamowienia_klientow")
    
    return cursor.fetchall()

def order_products():
    cursor.execute("SELECT * FROM sklep.zamowienie_produkty")
    
    return cursor.fetchall()

def make_order(order_detail, items):
    id_order = orders()
    id_order = id_order[-1][0] + 1
    resp =  False
    time = date.today()
    
    delivery_cost = 15.0
    order_detail.insert(0, id_order)
    order_detail.insert(2, delivery_cost)
    order_detail.insert(3, time)

    try:
        cursor.execute("INSERT INTO sklep.zamowienie VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", order_detail)
        conn.commit()
        id_order_product = order_products()
        id_order_product = id_order_product[-1][0] + 1
        
        for id, cuantity in items:
                for product in p.products():
                    if product[0] == id:                    
                        cursor.execute("INSERT INTO sklep.zamowienie_produkty VALUES(%s, %s, %s, %s, %s)", [id_order_product, id_order, id, product[1], cuantity])
                        id_order_product +=1
                        
                        conn.commit() 
                        resp =  True

    except:
        cursor.execute("ROLLBACK")
        conn.commit()

        
    return resp


