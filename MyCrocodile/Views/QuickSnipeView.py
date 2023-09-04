
from MyCrocodile.CrocoUtils.Packages import *
from MyCrocodile.CrocoUtils.FilterGenerator import *
from MyCrocodile.CrocoUtils.Helpers import *
from MyCrocodile.Views.Console import *

# import tkinter as tk
from tkinter import *
import tkinter as tk
import ttkbootstrap as tb
from tkinter import messagebox as msg
from tkinter.ttk import Notebook
from tkinter import filedialog

# from ttkbootstrap.constants import *


BIG_FONT= ('Helvetica', '30')
SMALL_FONT= ('Helvetica', '15')


class QuickSnipeView(tb.Frame):
    
    def __init__(self,master=None,bootstyle='yeti'):
        super().__init__(master, bootstyle=bootstyle)
        self.label = {}
        self.comboboxes = {}
        self.rowconfigure(0, weight=1)
        # for i in range(2):
        #     self.columnconfigure(i, weight=1)
        self.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        
        self.parentQueue = queue.Queue()
        
        #* GLOBAL VARIABLES
        self.STATS_VAR_COUNT = 0
        self.GUI_STATS_VARS = {}
        
        #* default value lists for UI
        self.GapTimeList = [0,1,2,3,4,5,6,7,8,9,10]
        self.CyclesList = [1,2,3,4,5,6]
        
        #* Read the default config status 
        print(os. getcwd())
        self.config = configparser.ConfigParser(allow_no_value=True)
        self.config.read("./MyCrocodile/Resources/settings.ini")
        print(self.config.options('Statistics'))
        
        #? Create variables for bot tracking stats
        GUIClearStats(self.config) #? clear the config
        
        stats_options = self.config.options('Statistics') #? return a list
        for useroption in stats_options:
            var = tk.StringVar(name=str(useroption))
            value = self.config.get("Statistics", useroption)
            var.set(str(value))
            self.GUI_STATS_VARS[useroption] = var
        
        #! Create everything here
        self.CreateInputFrame()
        # self.CreateStatsFrame()
        self.CreateStatsDetailFrame()
        self.CreateSnipeMultiFrame()
        self.CreateBidFrame()


    def LabelEntry(self, master, Entryname, width=20):
        EntryFrame = tb.LabelFrame(master=master, text=Entryname)
        ThisEntry = tb.Entry(EntryFrame, width=width)
        ThisEntry.pack(padx=3,pady=3)


    def CreateInputFrame(self):
        self.InputFrame = tb.LabelFrame(self, text="Single Sniping Bot", bootstyle='info', width=25)
        self.InputFrame.grid(row=0,column=0,padx=5,pady=5,sticky='NSWE')
        # self.InputFrame.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        #! entries
        self.BuyPriceLabel = tb.Label(master=self.InputFrame, text='Buy Price: ', width=15)
        self.BuyPriceLabel.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.BuyPriceEntry = tb.Entry(master=self.InputFrame, textvariable=tk.StringVar(), width=10)
        self.BuyPriceEntry.grid(row=0, column=1, sticky='e', padx=5, pady=5)
        self.BuyPriceEntry.insert(0,'800')
        
        
        self.SearchPerLoopLabel = tb.Label(master=self.InputFrame, text='Search Per Loop: ', width=15)
        self.SearchPerLoopLabel.grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.SearchPerLoopEntry = tb.Entry(master=self.InputFrame, textvariable=tk.StringVar(), width=10)
        self.SearchPerLoopEntry.grid(row=1, column=1, sticky='e', padx=5, pady=5)
        self.SearchPerLoopEntry.insert(0,'20')
        
        
        self.GapTimeLabel = tb.Label(master=self.InputFrame, text='Gap Time: ', width=15)
        self.GapTimeLabel.grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.GapTimeEntry = tb.Entry(master=self.InputFrame, textvariable=tk.StringVar(), width=10)
        self.GapTimeEntry.grid(row=2, column=1, sticky='e', padx=5, pady=5)
        self.GapTimeEntry.insert(0,'3')
        
        
        self.LongBreakLabel = tb.Label(master=self.InputFrame, text='Long Break: ', width=15)
        self.LongBreakLabel.grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.LongBreakEntry = tb.Entry(master=self.InputFrame, textvariable=tk.StringVar(), width=10)
        self.LongBreakEntry.grid(row=3, column=1, sticky='e', padx=5, pady=5)
        self.LongBreakEntry.insert(0,'30')
        
        self.StartSnipeButton = tb.Button(master=self.InputFrame, text="Start Single Sniping", 
                                    bootstyle="danger", width=35)
        
        self.StartSnipeButton.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
        # self.FrameConsole = GUIconsole(self)
        # self.FrameConsole.pack(padx=10,pady=10)
        
    
    # def CreateStatsFrame(self):
        
    #     self.StatsFrame = tb.LabelFrame(self, text="Bot Statistics", bootstyle='info', width=25)
    #     self.StatsFrame.grid(row=1,column=0,padx=5,pady=5)
    #     # self.StatsFrame.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
    #     self.StatsLabel = tb.Label(master=self.StatsFrame, text="Total Search: 0\nTotal Bought: 0\nTotal Missed: 0")
    #     self.StatsLabel.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
    #     self.CoinUsedLabel = tb.Label(master=self.StatsFrame, text="Total coin used: 0")
    #     self.CoinUsedLabel.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
    #     self.StatsButton = tb.Button(master=self.StatsFrame, text="Get Statistics", width=25)
    #     self.StatsButton.pack(padx=10, pady=10, expand=True)
    
    
    def CreateStatsDetailFrame(self):
        self.StatsDetailFrame = tb.LabelFrame(self, text="Bot Live Stats", bootstyle='info', width=25)
        self.StatsDetailFrame.grid(row=1,column=0, sticky='NSWE', padx=3, pady=3)
        # self.StatsDetailFrame.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        self.BotStatsLabel = tb.Label(master=self.StatsDetailFrame, text="SearchedPlayers: 0\nBoughtPlayers: 0\nMissedPlayers: 0\n")
        self.BotStatsLabel.pack(padx=3, pady=3, fill=tk.BOTH, expand=True)
        
        self.BotCoinLabel = tb.Label(master=self.StatsDetailFrame, text="CoinHave: 0\nCoinUsed: 0\n")
        self.BotCoinLabel.pack(padx=3, pady=3, fill=tk.BOTH, expand=True)
        
        self.BotPlayerLabel = tb.Label(master=self.StatsDetailFrame, text="PlayerName: None\nPlayerPosition: None\nPlayerRating: None\n")
        self.BotPlayerLabel.pack(padx=3, pady=3, fill=tk.BOTH, expand=True)
        
        self.BotStatsButton = tb.Button(master=self.StatsDetailFrame, text="Update BotStats", width=25)
        self.BotStatsButton.pack(padx=3, pady=3, expand=True, fill=tk.BOTH)


    def CreateSnipeMultiFrame(self):
        self.SnipeMultiFrame = tb.LabelFrame(self, text = 'Multiple Sniping Bot', bootstyle='info', width=30)
        self.SnipeMultiFrame.grid(row=0,column=1,padx=5,pady=5, sticky='NSWE')

        self.TemplateButton = tb.Button(master=self.SnipeMultiFrame, text="Download .csv template",
                            bootstyle="info", width=25)

        self.TemplateButton.grid(row=0,column=0,columnspan=2)
        
        #! entries
        self.MultiSearchPerLooplb = tb.Label(master=self.SnipeMultiFrame, text='Search per loop: ', width=15)
        self.MultiSearchPerLooplb.grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.MultiSearchPerLoop = tb.Entry(master=self.SnipeMultiFrame, textvariable=tk.StringVar(), width=10)
        self.MultiSearchPerLoop.grid(row=1, column=1, sticky='e', padx=5, pady=5)
        self.MultiSearchPerLoop.insert(0,'15')
        
        #! entries
        self.MultiGapTimelb = tb.Label(master=self.SnipeMultiFrame, text='Gap Time: ', width=15)
        self.MultiGapTimelb.grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.MultiGapTime = tb.Entry(master=self.SnipeMultiFrame, textvariable=tk.StringVar(), width=10)
        self.MultiGapTime.grid(row=2, column=1, sticky='e', padx=5, pady=5)
        self.MultiGapTime.insert(0,'3')
        
        #! entries
        self.MultiLongBreaklb = tb.Label(master=self.SnipeMultiFrame, text='Long Break: ', width=15)
        self.MultiLongBreaklb.grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.MultiLongBreak = tb.Entry(master=self.SnipeMultiFrame, textvariable=tk.StringVar(), width=10)
        self.MultiLongBreak.grid(row=3, column=1, sticky='e', padx=5, pady=5)
        self.MultiLongBreak.insert(0,'15')
        
        
        #! Button
        self.MultiUploadButton = tb.Button(master=self.SnipeMultiFrame,text="Upload .csv input file", 
                                            bootstyle='success', width=35)
        self.MultiUploadButton.grid(row=4, column=0, padx=5, pady=5, columnspan=2)
        
        #! Button
        self.MultiStartButton = tb.Button(master=self.SnipeMultiFrame, text="Start Multiple Sniping", 
                                    bootstyle="warning", width=35)
        self.MultiStartButton.grid(row=5, column=0, padx=5, pady=5, columnspan=2)
        


    def CreateBidFrame(self):
        
        
        self.BidFrame = tb.LabelFrame(self, text="Bid Bot Input", bootstyle='info', width=25)
        self.BidFrame.grid(row=1,column=1,padx=5,pady=5,sticky='NSWE')
        # self.InputFrame.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        #! entries
        self.BidPriceLabel = tb.Label(master=self.BidFrame, text='Max Bid Price: ', width=15)
        self.BidPriceLabel.grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.BidPriceEntry = tb.Entry(master=self.BidFrame, textvariable=tk.StringVar(), width=10)
        self.BidPriceEntry.grid(row=0, column=1, sticky='e', padx=5, pady=5)
        self.BidPriceEntry.insert(0,'700')
        
        
        self.BidCycleLabel = tb.Label(master=self.BidFrame, text='Bid Cycle: ', width=15)
        self.BidCycleLabel.grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.BidCycleEntry = tb.Entry(master=self.BidFrame, textvariable=tk.StringVar(), width=10)
        self.BidCycleEntry.grid(row=1, column=1, sticky='e', padx=5, pady=5)
        self.BidCycleEntry.insert(0,'5')
        
        
        self.ItemPerPageLabel = tb.Label(master=self.BidFrame, text='Item per page: ', width=15)
        self.ItemPerPageLabel.grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.ItemPerPageEntry = tb.Entry(master=self.BidFrame, textvariable=tk.StringVar(), width=10)
        self.ItemPerPageEntry.grid(row=2, column=1, sticky='e', padx=5, pady=5)
        self.ItemPerPageEntry.insert(0,'5')
        
        
        self.BidBreakLabel = tb.Label(master=self.BidFrame, text='Bid Break: ', width=15)
        self.BidBreakLabel.grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.BidBreakEntry = tb.Entry(master=self.BidFrame, textvariable=tk.StringVar(), width=10)
        self.BidBreakEntry.grid(row=3, column=1, sticky='e', padx=5, pady=5)
        self.BidBreakEntry.insert(0,'30')
        
        self.StartBidWar = tb.Button(master=self.BidFrame, text="Start Bid War", 
                                    bootstyle="danger", width=35)
        
        self.StartBidWar.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
