from CrocoUtils.Packages import *
from tkinter.ttk import Notebook
from tkinter import filedialog


class SnipeController():

    def __init__(self, model, view) -> None:
        
        self.model = model
        self.view = view
        # self.view.buttons['RunBuyAndStore'].configure(command= lambda: threading.Thread(target = self.five_seconds, daemon=True).start())
        self.view.StartSnipeButton.configure(command = lambda: threading.Thread(target = self.RunBuyAndStoreClick, daemon=True).start())
        self.view.BotStatsButton.configure(command = lambda: threading.Thread(target = self.UpdateBotStats, daemon=True).start())
        
        self.view.MultiUploadButton.configure(command = lambda: threading.Thread(target = self.UploadCSVInput, daemon=True).start())
        self.view.MultiStartButton.configure(command = lambda: threading.Thread(target = self.BuyAndStoreWithCSVInput, daemon=True).start())

        self.view.StartBidWar.configure(command = lambda: threading.Thread(target = self.RunSearchGetBid, daemon=True).start())


    def RunSearchGetBid(self):
        print("New thread is created for BuyAndStore")
        
        InputData= {
            'BidPrice': int(self.view.BidPriceEntry.get()),
            'BidCycle': int(self.view.BidCycleEntry.get()),
            'MaxBid': int(self.view.BidPriceEntry.get()),
            'listmax': int(self.view.ItemPerPageEntry.get())
        }
        
        self.model.SearchGetBid(**InputData)
    
    
    def RunBuyAndStoreClick(self):
        print("New thread is created for BuyAndStore")
        
        InputData= {
            'BuyPrice': float(self.view.BuyPriceEntry.get()),
            'SearchPerLoop': int(self.view.SearchPerLoopEntry.get()),
            'SleepTime': float(self.view.GapTimeEntry.get()),
            'LongBreak': float(self.view.LongBreakEntry.get()),
            'FirstOnly':True
        }
        
        self.model.RunBuyAndStore(**InputData)
    
    
    def UploadCSVInput(self):
        print("New thread is created for BuyAndStore")
        self.filename = filedialog.askopenfilename()
        print(self.filename)


    def BuyAndStoreWithCSVInput(self):
        print("New Thread is created for BuyAndStoreWithCSVInput ")
        InputData= {
            'SetMaxMinBid':1000,
            'SearchPerLoop': int(self.view.MultiSearchPerLoop.get()),
            'SleepTime': float(self.view.MultiGapTime.get()),
            'LongBreak': float(self.view.MultiLongBreak.get())
        }
        InputData['CSVinput'] = self.filename
        
        while(True):
            self.model.RunBuyAndStoreWithCSVInput(**InputData)
            self.model.SleepGen(float(InputData['LongBreak']))



    def UpdateBotStats(self):
        # print("New Thread is created for UpdateBotStats ")
        
        StatsLogs = "SearchedPlayers: {}\nBoughtPlayers: {}\nMissedPlayers: {}\n".format(self.model.SearchedPlayers,
                                                                                        self.model.BoughtPlayers,
                                                                                        self.model.MissedPlayers)
        CoinLogs = "CoinHave: {}\nCoinUsed: {}\n".format(self.model.CoinHave, self.model.CoinUsed)
        PlayerLogs = "PlayerName: {}\nPlayerPosition: {}\nPlayerRating: {}\n".format(self.model.PlayerName,
                                                                                    self.model.PlayerPosition,
                                                                                    self.model.PlayerRating)
        
        
        self.view.BotStatsLabel.config(text = StatsLogs)
        self.view.BotCoinLabel.config(text = CoinLogs)
        self.view.BotPlayerLabel.config(text = PlayerLogs)