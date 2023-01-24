from tkinter import *
from tkinter import ttk

class Table:
    def __init__(self, root, headings, sizes, values):
        self.root=root
        self.table_scroll = Scrollbar(self.root)
        self.table_scroll.pack(side=RIGHT, fill=Y)

        self.table = ttk.Treeview(self.root, yscrollcommand=self.table_scroll.set)

        self.table_scroll.config(command=self.table.yview)

        self.table['columns'] = headings
        
        self.table.column("#0", width=0,  stretch=NO)
        self.table.heading("#0",text="",anchor=CENTER)

        for size, heading in zip(sizes, headings):
            self.table.column(heading, anchor=CENTER, width=size)
            self.table.heading(heading,text=heading,anchor=CENTER)

        for i, value in enumerate(values):
            self.table.insert(parent='',index='end',iid=i,text='', values=value)

    def pack(self):
        self.table.pack()

    def delete(self):
        self.table.destroy()
        self.table_scroll.destroy()

    def update(self, headings, sizes, values):
        self.delete()

        self.table_scroll = Scrollbar(self.root)
        self.table_scroll.pack(side=RIGHT, fill=Y)

        self.table = ttk.Treeview(self.root,yscrollcommand=self.table_scroll.set)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Courier New", 10, 'bold'))

        self.table_scroll.config(command=self.table.yview)

        self.table['columns'] = headings
        
        self.table.column("#0", width=0,  stretch=NO)
        self.table.heading("#0",text="",anchor=CENTER)

        for size, heading in zip(sizes, headings):
            self.table.column(heading, anchor=CENTER, width=size)
            self.table.heading(heading,text=heading,anchor=CENTER)

        for i, value in enumerate(values):
            self.table.insert(parent='',index='end',iid=i,text='', values=value)
