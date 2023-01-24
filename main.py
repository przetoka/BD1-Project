from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import base_connection.layout as l
import base_connection.employees as e

class main_window:
    def __init__(self):
        self.button_bg = '#5D9128'
        self.regular_bg = '#CCEEBA'
        self.font = ("Courier New", 20)
        self.font_big =("Courier New", 25)
        self.window = Tk()
        self.window.configure(bg=self.regular_bg)
        self.window.title('sklep')
        self.window.geometry('1600x910')

        self.style = ttk.Style()
        self.style.configure("BW.TLabel", background=self.regular_bg, font=self.font)

        log_frame = ttk.Frame(self.window, padding=10, style='BW.TLabel')
        log_frame.pack(side = TOP)
        log_data_frame = ttk.Frame(log_frame, padding=1, style='BW.TLabel')
        log_data_frame.pack(side = LEFT)

        self.email_frame = ttk.Frame(log_data_frame, padding=1, style='BW.TLabel')
        self.email_frame.pack(side = TOP)
        self.password_frame = ttk.Frame(log_data_frame, padding=1, style='BW.TLabel')
        self.password_frame.pack(side = BOTTOM)

        self.buttons_log_in_out = ttk.Frame(log_frame, padding=1, style='BW.TLabel')
        self.buttons_log_in_out.pack(side = LEFT)


        self.email_label = Label(self.email_frame, text='email: ', bg=self.regular_bg, width=10,font=self.font)
        self.email_label.pack(side = LEFT)
        self.email = Entry(self.email_frame, width = 30,font=self.font)
        self.email.pack(side=LEFT)

        self.pass_label = Label(self.password_frame, text='hasło: ', bg=self.regular_bg, width=10,font=self.font)
        self.pass_label.pack(side = LEFT)
        self.password = Entry(self.password_frame, width = 30,font=self.font)
        self.password.pack(side=LEFT)

        # log_text = Label(log_frame, bg=self.regular_bg, text='  ').pack(side = LEFT)
        self.log_button = Button(self.buttons_log_in_out, text='zaloguj',fg='black', font=self.font, bg=self.button_bg, command=self.login_employee)
        self.log_button.pack(side = TOP)


        Label(log_frame, bg=self.regular_bg,fg='black', font=self.font, text='  aktywny pracownik: ').pack(side = LEFT)
        self.log_data = Label(log_frame, bg=self.regular_bg,fg='black', font=self.font, text='- ', width=20)
        self.log_data.pack(side = RIGHT)


        main_frame = ttk.Frame(self.window, style='BW.TLabel')
        main_frame.pack()

        main_menu_frame = ttk.Frame(main_frame, style="BW.TLabel", padding=20)
        main_menu_frame.pack(side = LEFT)

        data_frame = ttk.Frame(main_frame, style='BW.TLabel')
        data_frame.pack(side = RIGHT)

        self.tables = l.layout(data_frame, 'BW.TLabel')
        self.tables.update('shop')
        self.tables.show()

        shop=lambda:self.tables.update('shop')
        warehouse=lambda:self.tables.update('warehouse')
        product=lambda:self.tables.update('product')
        employee=lambda:self.tables.update('employee')
        client=lambda:self.tables.update('client')
        order=lambda:self.tables.update('order')

        labels = ["Sklepy", "Magazyny", 'Produkty',"Pracownicy", "Klienci", "Zamowienia"]
        functions=[shop, warehouse, product, employee, client, order]
        # self.buttons = []

        for func, label in zip(functions, labels):
            button = Button(main_menu_frame, text=label, font=self.font,fg='black', bg=self.button_bg, width=12, height=3, command=func)
            button.pack(side = TOP)
            Label(main_menu_frame, bg=self.regular_bg, text='').pack()

            # self.buttons.append(button)


        self.window.mainloop()

    def login_employee(self):
        result = e.login(self.email.get(),  self.password.get())
        if result != []:
            self.tables.set_active_employee(result[0][0])
            self.log_data['text'] = result[0][1:3]
            self.email.delete(0, END)
            self.password.delete(0, END)
            messagebox.showinfo('Informacja', 'Zalogowano')
            self.log_button.destroy()
            self.email_label.destroy()
            self.email.destroy()
            self.pass_label.destroy()
            self.password.destroy()
            self.logout_button = Button(self.buttons_log_in_out, text='wyloguj',fg='black', font=self.font, bg=self.button_bg, command=self.logout_employee)
            self.logout_button.pack(side = BOTTOM)
            
        else:
            messagebox.showinfo('Informacja', 'Złe dane logowania')

    def logout_employee(self):
        self.tables.set_inactive_employee()
        self.logout_button.destroy()
        self.email_label = Label(self.email_frame, text='email: ', bg=self.regular_bg, width=10,font=self.font)
        self.email_label.pack(side = LEFT)
        self.email = Entry(self.email_frame, width = 30,font=self.font)
        self.email.pack(side=LEFT)

        self.pass_label = Label(self.password_frame, text='hasło: ', bg=self.regular_bg, width=10,font=self.font)
        self.pass_label.pack(side = LEFT)
        self.password = Entry(self.password_frame, width = 30,font=self.font)
        self.password.pack(side=LEFT)
        
        self.log_button = Button(self.buttons_log_in_out, text='zaloguj',fg='black', font=self.font, bg=self.button_bg, command=self.login_employee)
        self.log_button.pack(side = TOP)
        
        self.log_data['text'] = '-'
        messagebox.showinfo('Informacja', 'Wylogowano')


main_window()