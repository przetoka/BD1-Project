from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter import messagebox

import base_connection.Table as Table

import base_connection.shops as s
import base_connection.warehouses as w
import base_connection.products as p
import base_connection.employees as e
import base_connection.clients as c
import base_connection.orders as o


font = ("Courier New", 13)
font_big = ("Courier New", 20)
font_bigger = ("Courier New", 25)
font_huge = ("Courier New", 30)
button_bg = '#5D9128'
regular_bg = '#CCEEBA'

class layout:
    def __init__(self, root, style):
        self.root = root
        self.style=style
        
        self.buttons_frame              = ttk.Frame(self.root, padding=25, style=self.style)
        self.table_frame                = ttk.Frame(self.root, padding=25, style=self.style)
        self.add_product_frame          = ttk.Frame(self.root, padding=25, style=self.style)
        self.add_record                 = Button(self.buttons_frame, text='dodaj rekord', font=font, fg='black', bg=button_bg, command=self.add)
        self.add_to_shop                = Button(self.add_product_frame, text='dodaj do sklepu', font=font, fg='black', bg=button_bg, command=self.add_product)
        self.add_to_warehouse           = Button(self.add_product_frame, text='dodaj do magazynu', font=font, fg='black', bg=button_bg, command=self.add_product)
        self.spacer                     = Label(self.buttons_frame, text=' ',bg=regular_bg, width = 50)
        self.combobox                   = ttk.Combobox(self.buttons_frame, values=[], width=30, font=font_big)
        self.change_table               = Button(self.buttons_frame, text='zmien tabele', font=font, fg='black', bg=button_bg, command=self.upd_table)
        self.table                      = Table.Table(self.table_frame, [], [], [])
        
        self.add_record['state'] = DISABLED
        self.add_to_shop['state'] = DISABLED
        self.add_to_warehouse['state'] = DISABLED

        self.buttons_frame.pack(side = TOP)
        self.table_frame.pack(side = BOTTOM)

    # headings of tables from the database
        self.shops_heading          = ['id sklepu', 'miasto', 'ulica', 'kod pocztowy', 'nr domu', 'nr mieszkania']
        self.warehouses_heading     = ['id magazynu', 'miasto', 'ulica', 'kod pocztowy', 'nr domu', 'nr mieszkania']
        self.products_heading       = ['id produktu', 'cena', 'nazwa', 'opis', 'kategoria']
        self.employees_heading      = ['id', 'imie', 'nazwisko', 'id sklepu', 'id magazynu', 'nr telefonu', 'email', 'rola']
        self.clients_heading        = ['id klienta', 'imie', 'nazwisko', 'email', 'nr telefonu', 'miasto', 'ulica', 'kod pocztowy', 'nr domu', 'nr mieszkania']
        self.orders_heading         = ['id zamowienie', 'id klient', 'cena dostawy', 'data zlozenia', 'status zamowienia', 'sposob platnosci', 'status platnosci', 'id pracownik']
    # sizes of tables from the database
        self.shops_sizes            = (210, 210, 210, 210, 210, 210)
        self.warehouses_sizes       = (210, 210, 210, 210, 210, 210)
        self.products_sizes         = (252, 252, 252, 252, 252)
        self.employees_sizes        = (120, 220, 220, 130, 130, 130, 250, 60)
        self.clients_sizes          = (100, 120, 120, 220, 130, 120, 120, 120, 100, 110)
        self.orders_sizes           = (160, 160, 160, 150, 150, 160, 160, 160)
    # headings of tables from views
        self.sh_employees_heading   = ['id sklepu', 'miasto', 'ulica', 'nr domu', 'nr mieszkania', 'imie', 'nazwisko', 'email', 'nr telefonu', 'rola']
        self.wh_employees_heading   = ['id magazynu', 'miasto', 'ulica', 'nr domu', 'nr mieszkania', 'imie', 'nazwisko', 'email', 'nr telefonu', 'rola']
        self.sh_products_heading    = ['id produktu', 'nazwa', 'id sklepu', 'ilosc', 'miasto', 'ulica', 'nr domu', 'nr mieszkania']
        self.wh_products_heading    = ['id produktu', 'nazwa', 'id magazynu', 'ilosc', 'miasto', 'ulica', 'nr domu', 'nr mieszkania']
        self.orders_outline_heading = ['id klient', 'imie', 'nazwisko', 'nr zam', 'łączny koszt produktow', 'cena dostawy', 'status zamowienia']
        self.order_products_heading = ['id klient', 'imie', 'nazwisko', 'nr zam', 'nazwa', 'opis', 'ilosc', 'cena jednego', 'cena wszytskich']
        self.clients_orders_heading = ['id klient', 'imie', 'nazwisko', 'nazwa najwiecej zam. produktu', 'opis', 'ilosc', 'łączna ilość zamówień klienta']
    # sizes of tables from views
        self.sh_employees_sizes     = (100, 100, 100, 120, 120, 100, 100, 220, 100, 200)
        self.wh_employees_sizes     = (100, 100, 100, 120, 120, 100, 100, 220, 100, 200)
        self.sh_products_sizes      = (160, 160, 170, 150, 140, 160, 160, 160)
        self.wh_products_sizes      = (160, 160, 170, 150, 140, 160, 160, 160)
        self.orders_outline_sizes   = (160, 160, 160, 150, 250, 160, 220)
        self.order_products_sizes   = (160, 160, 160, 70, 150, 160, 90, 140, 160)
        self.clients_orders_sizes   = (150, 150, 150, 300, 180, 80, 250)

        self.combobox_shops         = ['wszytskie sklepy', 'pracownicy sklepow', 'produkty w sklepach']
        self.combobox_warehouses    = ['wszytskie magazyny', 'pracownicy magazynow', 'produkty w magazynach']
        self.combobox_products      = ['wszystkie produkty', 'produkty w magazynach', 'produkty w sklepach']
        self.combobox_employees     = ['wszyscy pracownicy', 'pracownicy magazynow', 'pracownicy sklepow']
        self.combobox_clients       = ['wszyscy klienci', 'zamowienia klientow']
        self.combobox_orders        = ['wszytskie zamownienia', 'zarys zamowien', 'produkty zamowien', 'zamowienia klientow']
        

        self.current = ''
        self.current_headings       = []
        self.current_sizes          = []
        self.current_combobox       = []
        self.current_functions      = []
        self.current_add_function   = []

        self.shopping_cart = []
        self.shopping_cart_frames = []
        self.active_employee = None
    
    def show(self):
        self.add_to_shop.destroy()
        self.add_to_warehouse.destroy()
        self.add_record.pack(side = LEFT)
        self.add_product_frame.pack(side=BOTTOM)
        if self.current == 'shop':
            self.add_to_shop                = Button(self.add_product_frame, text='dodaj produkt do sklepu', font=font, fg='black', bg=button_bg, command=self.add_product)
            self.add_to_shop.pack(side=LEFT)
            if self.active_employee == None:
                self.add_to_shop['state'] = DISABLED
        if self.current == 'warehouse':
            self.add_to_warehouse           = Button(self.add_product_frame, text='dodaj produkt do magazynu', font=font, fg='black', bg=button_bg, command=self.add_product)
            self.add_to_warehouse.pack(side=LEFT)
            if self.active_employee == None:
                self.add_to_warehouse['state'] = DISABLED

        self.spacer.pack(side=LEFT)
        self.change_table.pack(side = LEFT)
        self.combobox.pack(side = LEFT)
        self.table.pack()

    def add_wh_sh(self, product):
        for p, e in self.add_items:
            if product[0]==p and e.get()!='':
                if self.current == 'shop':
                    val = s.shops()
                    s.add_item([val[self.cb.current()][0], p, e.get()])
                if self.current == 'warehouse':
                    val = w.warehouses()
                    w.add_item([val[self.cb.current()][0], p, e.get()])
                print(e.get())
            

    def close_product_form(self):
        self.product_form.destroy()
        self.add_items = []

    def add_product(self):
        self.product_form = Tk()
        self.product_form.config(width=800)

        choose_place = ttk.Frame(self.product_form, width= 700)
        choose_place.pack(side=TOP, padx=5, pady=5)

        add_products= ttk.Frame(self.product_form, width= 700)
        add_products.pack(side=TOP, padx=5, pady=5)

        if self.current == 'shop':
            name = 'sklep'
            self.cb = ttk.Combobox(choose_place, values=s.shops(), width=40, font=font)
        if self.current == 'warehouse':
            name = 'magazyn'
            self.cb = ttk.Combobox(choose_place, values=w.warehouses(), width=40, font=font)

        self.cb.pack(side = LEFT, padx=5, pady=5)
        self.product_form.title('dodaj produkt do ' + name)

        self.add_items = []
        for product in p.products():
            temp_frame = ttk.Frame(add_products, width= 700)
            temp_frame.pack(side = TOP, padx=5, pady=5)

            Label(temp_frame, text=product[2:4], font=font_big).pack(side = LEFT)
            temp_entry = Entry(temp_frame, width = 3,font=font_big)
            temp_entry.pack(side=LEFT)
            Button(temp_frame, text='dodaj',fg='black', width=8, height=1, font=font, bg=button_bg, command=partial(self.add_wh_sh, product)).pack(side = LEFT)

            self.add_items.append([product[0], temp_entry])
        
        Button(self.product_form, text='zamknij',fg='black', width=18, height=1, font=font, bg=button_bg, command=self.close_product_form).pack(side = RIGHT, padx=5, pady=5)

    def update(self, name):
        match name:
            case'shop':
                self.current = name
                self.current_headings   = [self.shops_heading, self.sh_employees_heading, self.sh_products_heading]
                self.current_sizes      = [self.shops_sizes, self.sh_employees_sizes, self.sh_products_sizes]
                self.current_combobox   = self.combobox_shops
                self.current_functions  = [s.shops(), e.shop_employees(), p.products_in_shops()]
                self.current_add_function =s.insert
            case 'warehouse':
                self.current = name
                self.current_headings   = [self.warehouses_heading, self.wh_employees_heading, self.wh_products_heading]
                self.current_sizes      = [self.warehouses_sizes, self.wh_employees_sizes, self.wh_products_sizes]
                self.current_combobox   = self.combobox_warehouses
                self.current_functions  = [w.warehouses(), e.warehouse_employees(), p.products_in_warehouses()]
                self.current_add_function =w.insert
            case'product':
                self.current = name
                self.current_headings   = [self.products_heading, self.wh_products_heading, self.sh_products_heading]
                self.current_sizes      = [self.products_sizes, self.wh_products_sizes, self.sh_products_sizes]
                self.current_combobox   = self.combobox_products
                self.current_functions  = [p.products(), p.products_in_warehouses(), p.products_in_shops()]
                self.current_add_function =p.insert
            case 'employee':
                self.current = name
                self.current_headings   = [self.employees_heading, self.sh_employees_heading, self.sh_employees_heading]
                self.current_sizes      = [self.employees_sizes, self.sh_employees_sizes, self.sh_employees_sizes]
                self.current_combobox   = self.combobox_employees
                self.current_functions  = [e.employees(), e.shop_employees(), e.warehouse_employees()]
                self.current_add_function =e.insert
            case'client':
                self.current = name
                self.current_headings   = [self.clients_heading, self.clients_orders_heading]
                self.current_sizes      = [self.clients_sizes, self.clients_orders_sizes]
                self.current_combobox   = self.combobox_clients
                self.current_functions  = [c.clients(), o.orders_clients()]
                self.current_add_function =c.insert
            case 'order':
                self.current = name
                self.current_headings   = [self.orders_heading, self.orders_outline_heading, self.order_products_heading, self.clients_orders_heading]
                self.current_sizes      = [self.orders_sizes, self.orders_outline_sizes, self.order_products_sizes, self.clients_orders_sizes]
                self.current_combobox   = self.combobox_orders
                self.current_functions  = [o.orders(), o.orders_outline(), o.orders_products(), o.orders_clients()]

        self.combobox.destroy()
        self.table.delete()
        self.combobox                   = ttk.Combobox(self.buttons_frame, values=self.current_combobox, state = 'readonly',width=30, font=font_big)
        value = self.current_functions[0]
        self.table                      = Table.Table(self.table_frame, self.current_headings[0], self.current_sizes[0], value)
        self.show()
    

    def delete_from_shopping_cart(self, product):
        for i, f in enumerate(self.shopping_cart_frames):
            if product==f[0]:
                f[1].destroy()
                self.shopping_cart_frames.pop(i)
                

        for i, e in enumerate(self.shopping_cart):
            if product[0] == e[0]:
                self.shopping_cart.pop(i)

    def check_shopping_cart(self, product):
        for i, e in enumerate(self.shopping_cart):
            if product[0] == e[0]:
                return [True, i]
        else:
            return [False]

    def add_item(self, product):
        for p, e in self.items:
            if product[0]==p and e.get()!='':
                t_o_f = self.check_shopping_cart(product)
                if t_o_f[0]:
                    self.shopping_cart[t_o_f[1]][1] +=  int(e.get())
                    self.shopping_cart_frames[t_o_f[1]][2].config(text = self.shopping_cart[t_o_f[1]][1])
                    
                else:
                    self.shopping_cart.append([p, int(e.get())])
                    
                    temp_frame = ttk.Frame(self.shopping_cart_form, width= 700)
                    temp_frame.pack(side = TOP)

                    Label(temp_frame, text=product[2:4], width=30, font=font_big).pack(side = LEFT, padx=5, pady=5)
                    ilosc = Label(temp_frame, text=self.shopping_cart[-1][1], font=font_big)
                    ilosc.pack(side = LEFT, padx=5, pady=5)
                    self.shopping_cart_frames.append([product, temp_frame, ilosc])
                    insert_button = Button(temp_frame, text='usun z koszyka',fg='black', width=12, height=1, font=font, bg=button_bg, command=partial(self.delete_from_shopping_cart, product))
                    insert_button.pack(side = LEFT)

    def set_active_employee(self, employee):
        self.active_employee = employee
        self.add_record['state'] = NORMAL
        self.show()
    
    def set_inactive_employee(self):
        self.active_employee = None
        self.add_record['state'] = DISABLED
        self.show()

    def close_order_form(self):
        self.shopping_cart = []
        self.items = []
        self.shopping_cart_frames = []
        self.order_form.destroy()

    def finalize_order(self):
        val = c.clients_order()
        client_id = val[self.client_cb.current()][0]
        payment_methods=['blik', 'przelew', 'przy odbiorze', 'opłacone z góry']
        payment_status=['opłacone', 'do zapłaty']
        self.payment_method.current()
        self.payment_status.current()
        self.shopping_cart
        
        
        response=o.make_order([client_id, 'w trakcie realizacji', payment_methods[self.payment_method.current()], payment_status[self.payment_status.current()], self.active_employee], self.shopping_cart)

        if(response):
            messagebox.showinfo('Informacja', 'Zamówienie zostało złożone')
            self.close_order_form()
        else:
            messagebox.showwarning('Błąd', 'Błąd przy składaniu zamówienia')
        

    def make_order_for_client(self):
        self.order_form = Tk()
        self.order_form.config(width=1400)
        self.order_form.title('złóż zamówienie')
    # top frame that contain products, client data and shopping cart
        top = ttk.Frame(self.order_form, width= 700)
        top.pack(side=TOP, padx=20, pady=20)
    # bottom frame that contains buttons to cancel or make order
        cancel_order_buttons = ttk.Frame(self.order_form, width= 1400)
        cancel_order_buttons.pack(side=BOTTOM, padx=20, pady=20)
    # buttons to cancel or make order
        Label(cancel_order_buttons, text='sposob płatności', font=font).pack(side = LEFT)
        self.payment_method = ttk.Combobox(cancel_order_buttons, values=['blik', 'przelew', 'przy odbiorze', 'opłacone z góry'], width=20, font=font)        
        self.payment_method.pack(side=LEFT, padx=10)
        Label(cancel_order_buttons, text='status płatności', font=font).pack(side = LEFT)
        self.payment_status = ttk.Combobox(cancel_order_buttons, values=['opłacone', 'do zapłaty'], width=20, font=font)        
        self.payment_status.pack(side=LEFT, padx=10)

        Label(cancel_order_buttons, text='', width=40, font=font).pack(side = LEFT)
        Button(cancel_order_buttons, text='złóż zamówienie',fg='black', width=18, height=1, font=font, bg=button_bg, command=self.finalize_order).pack(side = LEFT, padx=5, pady=5)
        Button(cancel_order_buttons, text='zamknij',fg='black', width=18, height=1, font=font, bg=button_bg, command=self.close_order_form).pack(side = LEFT, padx=5, pady=5)

    # form containing the shopping cart
        self.shopping_cart_form = ttk.Frame(top, width= 700)
        self.shopping_cart_form.pack(side=RIGHT, padx=5, pady=5)
        Label(self.shopping_cart_form, text='Koszyk', width=50, font=font_bigger).pack(side = TOP)


        order_products = ttk.Frame(top, width= 100)
        order_products.pack(side=TOP, padx=5, pady=5)
    # client data frame
        choose_client = ttk.Frame(order_products, width= 700)
        choose_client.pack(side=TOP, padx=5, pady=5)
    
        self.client_cb = ttk.Combobox(choose_client, values=c.clients_order(), width=80, font=font)        
        self.client_cb.pack(side=LEFT)

    # products scrollbar
        self.table_scroll = Scrollbar(order_products)
        self.table_scroll.pack(side=RIGHT, fill=Y)

        self.items = []
        for product in p.products():
            temp_frame = ttk.Frame(order_products, width= 700)
            temp_frame.pack(side = TOP, padx=5, pady=5)

            Label(temp_frame, text=product[2:4], width=40,font=font).pack(side = LEFT)
            temp_entry = Entry(temp_frame, width = 3,font=font)
            temp_entry.pack(side=LEFT)
            Button(temp_frame, text='dodaj',fg='black', width=8, height=1, font=font, bg=button_bg, command=partial(self.add_item, product)).pack(side = LEFT)

            self.items.append([product[0], temp_entry])
        
    def add(self):
        if self.current != 'order':
            insert_form = Tk()
            insert_form.configure(padx=20, pady=20)
            insert_form.title('formularz')
            self.insert_form =[]
            
            for label in self.current_headings[0]:
                temp_frame = ttk.Frame(insert_form, width= 700, style=self.style)
                temp_frame.pack(side = TOP)
                Label(temp_frame, text=label, font=font_big).pack(side = LEFT)
                temp_entry = Entry(temp_frame, font=font_big)
                self.insert_form.append(temp_entry)
                temp_entry.pack(side=RIGHT)
                Label(insert_form, text='', font=font).pack(side = TOP)
            
            log_frame = ttk.Frame(insert_form, style=self.style)
            log_frame.pack(side = TOP)

            insert_button = Button(log_frame, text='dodaj',fg='black', width=12, height=2, font=font, bg=button_bg, command=self.insert_data).pack(side = LEFT)
            close_button = Button(log_frame, text='zamknij',fg='black', width=12, height=2, font=font, bg=button_bg, command=insert_form.destroy).pack(side = LEFT)
            Label(insert_form, text='', font=font, bg=regular_bg).pack(side = BOTTOM)
        else:
            self.make_order_for_client()
        self.show()
    
    def insert_data(self):
        self.current_add_function([el.get() if el.get()!= '' else None for el in self.insert_form])
        self.table.pack()

    def upd_table(self):
        i =  self.combobox.current()
        self.table.update(self.current_headings[i], self.current_sizes[i], self.current_functions[i])

        self.table.pack()

    def delete(self):
        self.buttons_frame.destroy()
        self.table.delete()


