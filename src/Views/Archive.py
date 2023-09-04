from abc import abstractmethod
from doctest import master
from symbol import term

# from tkinter import *
# from tkinter import ttk
import tkinter as tk
# from tkinter import messagebox as msg
# from tkinter.ttk import Notebook
# from tkinter import filedialog


# import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class View(ttk.Frame):
    @abstractmethod
    def CreateView():
        raise NotImplementedError


class Form(View):
    def __init__(self, master=None):
        super().__init__(master)

        #? Initilize container
        self.master = master
        self.entries = {}
        self.buttons = {}
        self.label = {}
        self.comboboxes = {}
        
        #? Format
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=ttk.N + ttk.S + ttk.E + ttk.W)
    
    def CreateLabel(self, frame, label, text, row, column):
        LabelFrame = ttk.LabelFrame(master=frame, text=label, bootstyle="Primary")
        self.label[label] = tk.Label(master=LabelFrame,text=text)
        self.label[label].grid(row=0, column=0)
        LabelFrame.grid(row=row, column=column, sticky=ttk.N + ttk.S + ttk.E + ttk.W)
        

    def CreateEntry(self, frame, label, row, column, textvar):
        LabelFrame = ttk.LabelFrame(master=frame, text=label, bootstyle="Success")
        LabelFrame.grid(row=row, column=column,sticky='nsew')
        LabelFrame.rowconfigure(0, weight=1)
        LabelFrame.columnconfigure(0, weight=1)
        
        self.entries[label] = ttk.Entry(LabelFrame, textvariable=textvar)
        self.entries[label].grid(row=0,column=0,sticky='nsew')


    def CreateButton(self, frame, name, row, column):
        self.buttons[name] = ttk.Button(master=frame, bootstyle="danger")
        self.buttons[name]['text'] = name
        self.buttons[name].grid(row=row,column=column)


class SnipeView(Form):
    
    def __init__(self,master=None):
        super().__init__(master)
    
    def CreateSnipeView(self):

        self.CreateEntry(
            frame = self,
            label = 'BuyPrice',
            row = 0,
            column = 0,
            textvar = tk.DoubleVar()
        )
        
        self.CreateEntry(
            frame = self,
            label = 'Test',
            row = 1,
            column = 0,
            textvar = tk.DoubleVar()
        )
