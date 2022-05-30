import tkinter as tk
from tkinter import ttk

LABEL_FONT = ("Times bold", 14)

class Nav(tk.Frame):
  def __init__(self, parent, controller):
    self.controller = controller
    
    tk.Frame.__init__(self, parent, bg = "#5D8A82")

    button1 = ttk.Button(self, text = "Page 1", command = self.FirstPage)
    button1.grid(row = 0, column = 0, padx = 10, pady = 10)

    button2 = ttk.Button(self, text = "Page 2", command = self.SecondPage)
    button2.grid(row = 0, column = 1, padx = 10, pady = 10)

    button3 = ttk.Button(self, text = "Page 3", command = self.ThirdPage)
    button3.grid(row = 0, column = 2, padx = 10, pady = 10)

    button4 = ttk.Button(self, text = "Exit", command = self.Exit)
    button4.grid(row = 0, column = 3, padx = 10, pady = 10)

  def FirstPage(self):
    self.controller.show_frame("Page 1")

  def SecondPage(self):
    self.controller.show_frame("Page 2")

  def ThirdPage(self):
    self.controller.show_frame("Page 3")

  def Exit(self):
    self.controller.destroy()