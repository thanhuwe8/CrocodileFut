from abc import abstractmethod
from doctest import master
from symbol import term
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as msg
from tkinter.ttk import Notebook
from tkinter import filedialog


class View(tk.Frame):
    @abstractmethod
    def CreateView():
        raise NotImplementedError


class Form(View):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.entries = {}
        self.buttons = {}
        self.label = {}
        self.comboboxes = {}
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
    
    def CreateLabel(self, frame, label, text, row, column):
        LabelFrame = tk.LabelFrame(master=frame, text=label)
        self.label[label] = tk.Label(master=LabelFrame,text=text)
        self.label[label].grid(row=1, column=1)
        LabelFrame.grid(row=row, column=column, sticky=tk.N + tk.S + tk.E + tk.W)


    def CreateEntry(self, frame, label, row, column, textvar):
        LabelFrame = tk.LabelFrame(master=frame, text=label)
        self.entries[label] = tk.Entry(LabelFrame, textvariable=textvar)
        self.entries[label].grid(row=1,column=1)
        LabelFrame.grid(row=row, column=column, sticky=tk.N + tk.S + tk.E + tk.W)
    
    
    def CreateButton(self, frame, name, row, column):
        self.buttons[name] = tk.Button(master=frame)
        self.buttons[name]['text'] = name
        self.buttons[name].grid(row=row,column=column)
    
    
    def CreateCombobox(self, frame, label, values, row, column):
        LabelFrame = tk.LabelFrame(master=frame, text=label)
        self.comboboxes[label] = ttk.Combobox(LabelFrame, values=values)
        self.comboboxes[label].grid(row=1,column=1)
        LabelFrame.grid(row=row, column=column, sticky=tk.N + tk.S + tk.E + tk.W)
    
    
    def CreateViewSnipe(self):
        
        ControlFrame = tk.LabelFrame(master=self, text="InputData")
        ControlFrame.rowconfigure(0,weight=1)
        ControlFrame.columnconfigure(0,weight=1)
        ControlFrame.grid(row=1,column=0,sticky=tk.N + tk.S + tk.E + tk.W)
        
        OutputFrame = tk.LabelFrame(master=self, text="OutputStats")
        OutputFrame.rowconfigure(0,weight=1)
        OutputFrame.columnconfigure(0,weight=1)
        OutputFrame.grid(row=1,column=1,sticky=tk.N + tk.S + tk.E + tk.W)
    
        self.CreateEntry(
            frame = ControlFrame,
            label = 'BuyPrice',
            row = 0,
            column = 1,
            textvar = tk.DoubleVar()
        )
        
        self.CreateEntry(
            frame = ControlFrame,
            label = 'SearchPerLoop',
            row = 1,
            column = 1,
            textvar = tk.IntVar()
        )
        
        self.CreateEntry(
            frame = ControlFrame,
            label = 'SleepTime',
            row = 2,
            column = 1,
            textvar = tk.DoubleVar()
        )
        
        self.CreateEntry(
            frame = ControlFrame,
            label = 'LongBreak',
            row = 3,
            column = 1,
            textvar = tk.DoubleVar()
        )
        
        self.CreateButton(
            frame = ControlFrame,
            name = 'RunBuyAndStore',
            row = 4,
            column = 1
        )
        
        #! Bot stats print out
        self.CreateLabel(
            frame = OutputFrame,
            label = "SearchStats",
            text = "SearchStats",
            row = 0,
            column = 1
        )
        
        self.CreateLabel(
            frame = OutputFrame,
            label = "PortfolioStats",
            text= "PortfolioStats",
            row = 1,
            column = 1
        )
        
        self.CreateButton(
            frame = OutputFrame,
            name = 'UpdateBotStats',
            row = 2,
            column = 1
        )

    def CreateViewFodder(self):
        ControlFrame = tk.LabelFrame(master=self, text="InputData")
        ControlFrame.rowconfigure(0,weight=1)
        ControlFrame.columnconfigure(0,weight=1)
        ControlFrame.grid(row=1,column=0,sticky=tk.N + tk.S + tk.E + tk.W)
        
        OutputFrame = tk.LabelFrame(master=self, text="OutputStats")
        OutputFrame.rowconfigure(0,weight=1)
        OutputFrame.columnconfigure(0,weight=1)
        OutputFrame.grid(row=1,column=1,sticky=tk.N + tk.S + tk.E + tk.W)
        
        
        self.CreateEntry(
            frame = ControlFrame,
            label = 'IterationEachFodder',
            row = 0,
            column = 1,
            textvar = tk.IntVar()
        )
        
        self.CreateEntry(
            frame = ControlFrame,
            label = 'SleepTime',
            row = 1,
            column = 1,
            textvar = tk.IntVar()
        )

        self.CreateButton(
            frame = ControlFrame,
            name = 'UploadFodderList',
            row = 2,
            column = 1
        )
        
        
    def CreateCSVInputView(self):
        ControlFrame = tk.LabelFrame(master=self, text="InputData")
        ControlFrame.rowconfigure(0,weight=1)
        ControlFrame.columnconfigure(0,weight=1)
        ControlFrame.grid(row=1,column=0,sticky=tk.N + tk.S + tk.E + tk.W)
        
        OutputFrame = tk.LabelFrame(master=self, text="OutputStats")
        OutputFrame.rowconfigure(0,weight=1)
        OutputFrame.columnconfigure(0,weight=1)
        OutputFrame.grid(row=1,column=1,sticky=tk.N + tk.S + tk.E + tk.W)
        
        
        self.CreateEntry(
            frame = ControlFrame,
            label = 'SearchPerLoop',
            row = 0,
            column = 1,
            textvar = tk.IntVar()
        )
        
        self.CreateEntry(
            frame = ControlFrame,
            label = 'SleepTime',
            row = 1,
            column = 1,
            textvar = tk.IntVar()
        )
        
        self.CreateEntry(
            frame = ControlFrame,
            label = 'LongBreak',
            row = 2,
            column = 1, 
            textvar = tk.DoubleVar()
        )

        self.CreateButton(
            frame = OutputFrame,
            name = 'UploadCSVInput',
            row = 0,
            column = 2
        )
        
        self.CreateButton(
            frame = OutputFrame,
            name = 'BuyAndStoreWithCSVInput',
            row = 1,
            column = 2
        )
    
    def CreateDeepdiveMarketView(self):
        ControlFrame = tk.LabelFrame(master=self, text="InputData")
        ControlFrame.rowconfigure(0,weight=1)
        ControlFrame.columnconfigure(0,weight=1)
        ControlFrame.grid(row=1,column=0,sticky=tk.N + tk.S + tk.E + tk.W)
        
        OutputFrame = tk.LabelFrame(master=self, text="OutputStats")
        OutputFrame.rowconfigure(0,weight=1)
        OutputFrame.columnconfigure(0,weight=1)
        OutputFrame.grid(row=1,column=1,sticky=tk.N + tk.S + tk.E + tk.W)
        
        self.CreateEntry(
            frame = ControlFrame,
            label = 'Name',
            row = 0,
            column = 1,
            textvar = tk.IntVar()
        )
        
        self.CreateEntry(
            frame = ControlFrame,
            label = 'Rarity',
            row = 1,
            column = 1 ,
            textvar = tk.IntVar()
        )
        
        self.CreateEntry(
            frame = ControlFrame,
            label = 'Chemistry',
            row = 2,
            column = 1,
            textvar = tk.IntVar()
        )
        
        self.CreateEntry(
            frame = ControlFrame,
            label = 'PriceGuess',
            row = 3,
            column = 1,
            textvar = tk.IntVar()
        )
        
        self.CreateButton(
            frame = ControlFrame,
            name = 'MarketScan',
            row = 4,
            column = 1
        )
        
        self.CreateButton(
            frame = ControlFrame,
            name = 'BruteForceScan',
            row = 5,
            column = 1
        )
        
        #! Output
        list_of_label = ['Name', 'Rarity', 'BuyNowPrice', 'Liquidity']
        
        
        for index, item in enumerate(list_of_label):
            self.CreateLabel(
                frame = OutputFrame,
                label = item,
                text = "Output for {}: ".format(item),
                row = index + 1,
                column = 2
            )
        