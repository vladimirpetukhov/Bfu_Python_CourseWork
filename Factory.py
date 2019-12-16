import tkinter as tk
from tkinter import messagebox
from IFactory import IFactory
from services import Service
from db import DbContext as db


class Factory(IFactory):
    def __init__(self, master, db):
        super().__init__(master, db,selected_item=0)
        self.master = master
        self.db=db
        

