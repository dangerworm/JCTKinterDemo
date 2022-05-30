import tkinter as tk
from tkinter import ttk

LABEL_FONT = ("Times bold", 14)

class Page1(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)

    label = ttk.Label(self, text = "Page 1", font = LABEL_FONT)
    label.grid(row = 1, column = 1, padx = 10, pady = 10)
