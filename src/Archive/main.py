# CrocodileFut library
from View import *
from Model import *
from Controller import *

# del View
# del Model
# del Controller


# GUI library
from tkinter import ttk
import tkinter as tk

# Utilities
from threading import *


#! class application:

class Application(ttk.Notebook):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=tk.N + tk.W)
    
    def NewTab(self, controller, view, name):
        view = view(self.master) # functional refactor
        controller.bind(view)
        self.add(view, text=name)



if __name__ == "__main__":
    driver = uc.Chrome()
    # driver.get("https://www.futbin.com/")
    driver.set_window_size(1500, 1060)
    driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")


    root = tk.Tk()
    root.iconbitmap("main.ico")
    root.title("CrocodileFutTrading")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.geometry("300x900")


    app = Application(master=root)
    Model = CrocodileTrader(driver=driver)
    Controller1 = SnipeController(model=Model)
    Controller2  = CSVInputController(model=Model)


    app.NewTab(view=Form, controller=Controller1, name="MLSniping")
    app.NewTab(view=Form, controller=Controller2, name="CSVSniping")

    app.mainloop()



