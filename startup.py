import tkinter as tk
from Factory import Factory


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Part Manager')
        # Width height
        master.geometry("700x350")
        # Create widgets/grid
        factory = Factory(self.master)
        factory.create_widgets()
