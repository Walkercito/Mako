import tkinter as tk
from tkinter.font import Font
from tkinter import ttk

import sv_ttk

class MakacoUI(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        
        self.my_font = Font(family="YouTube Sans")
        
        self.link_entry = ttk.Entry(
            self.master,
            font=self.my_font,
            width=50
        )
        self.link_entry.place(relx=0.5, rely=0.5, anchor="center")