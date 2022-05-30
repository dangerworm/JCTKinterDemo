import tkinter as tk
from tkinter import LabelFrame

from Page1 import Page1
from Page2 import Page2
from Page3 import Page3
from Nav import Nav

pages = {
  "Page 1": Page1,
  "Page 2": Page2,
  "Page 3": Page3,
}

first_page = "Page 1"

class App(tk.Tk):
  def __init__(self, *args, **kwargs):
    self.frames = {}
    self.current_frame = ""

    tk.Tk.__init__(self, *args, **kwargs)

    main_frame = tk.Frame(self, width = 400, height = 300,
                          bg = "#5D8A82", padx = 10, pady = 10)

    navigation = tk.LabelFrame(main_frame, text = "Nav", bg = "#5D8A82",
                               padx = 0, pady = 0, height = 50)
    nav_frame = Nav(navigation, self)
    nav_frame.pack(expand = True, fill = 'both')

    content = tk.LabelFrame(main_frame, text = "Content", bg = "#5D8A82",
                            padx = 15, pady = 15, height = 250)

    for name in pages.keys():
      frame = pages[name](content, self)
      frame.grid(row = 0, column = 0, sticky = "nsew")
      self.frames[name] = frame

    for frame in [main_frame, content, navigation]:
      frame.pack(expand = True, fill = 'both')
      frame.pack_propagate(0)

    self.show_frame(first_page)
   
  def show_frame(self, name):
    content_frame = self.frames[name]

    if self.current_frame != "":
      self.current_frame.pack_forget()
      self.current_frame = content_frame

    content_frame.tkraise()
    self.current_frame = content_frame

app = App()

app.geometry('410x300')
app.title('Python Guides')

app.mainloop()
