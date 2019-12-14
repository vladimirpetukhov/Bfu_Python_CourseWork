import tkinter as tk
from IFactory import IFactory


class Factory(IFactory):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

    def create_widgets(self):
         #Part
        self.part_text=tk.StringVar()
        self.part_label=self.part_label = tk.Label(
        self.master, text='Part Name', font=('bold', 14), pady=20)
        self.part_label.grid(row=0, column=0, sticky=tk.W)
        self.part_entry = tk.Entry(self.master, textvariable=self.part_text)
        self.part_entry.grid(row=0, column=1)

        # Customer
        self.customer_text = tk.StringVar()
        self.customer_label = tk.Label(
            self.master, text='User', font=('bold', 14))
        self.customer_label.grid(row=0, column=2, sticky=tk.W)
        self.customer_entry = tk.Entry(
            self.master, textvariable=self.customer_text)
        self.customer_entry.grid(row=0, column=3)

        # Retailer
        self.retailer_text = tk.StringVar()
        self.retailer_label = tk.Label(
            self.master, text='Retailer', font=('bold', 14))
        self.retailer_label.grid(row=1, column=0, sticky=tk.W)
        self.retailer_entry = tk.Entry(
            self.master, textvariable=self.retailer_text)
        self.retailer_entry.grid(row=1, column=1)
        # Price
        self.price_text = tk.StringVar()
        self.price_label = tk.Label(
            self.master, text='Price', font=('bold', 14))
        self.price_label.grid(row=1, column=2, sticky=tk.W)
        self.price_entry = tk.Entry(self.master, textvariable=self.price_text)
        self.price_entry.grid(row=1, column=3)

        # Parts list (listbox)
        self.parts_list = tk.Listbox(self.master, height=8, width=50, border=0)
        self.parts_list.grid(row=3, column=0, columnspan=3,
                             rowspan=6, pady=20, padx=20)
        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=3, column=3)
        # Set scrollbar to parts
        self.parts_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.parts_list.yview)
