from View import *
from Model import *
from abc import ABC
import threading
import time
import random


class Controller(ABC):
    @abstractmethod
    def bind(view: View):
        raise NotImplementedError


class SnipeController(Controller):
    def __init__(self, model:CrocodileTrader) -> None:
        self.model = model
        self.view = None


    def bind(self, view: Form):
        self.view = view
        self.view.CreateViewSnipe()
        # self.view.buttons['RunBuyAndStore'].configure(command= lambda: threading.Thread(target = self.five_seconds, daemon=True).start())
        self.view.buttons['RunBuyAndStore'].configure(command = lambda: threading.Thread(target = self.RunBuyAndStoreClick, daemon=True).start())
        self.view.buttons['UpdateBotStats'].configure(command = lambda: threading.Thread(target = self.UpdateBotStats, daemon=True).start())


    def RunBuyAndStoreClick(self):
        print("New thread is created for BuyAndStore")
        
        InputData= {
            'BuyPrice': float(self.view.entries['BuyPrice'].get()),
            'SearchPerLoop': int(self.view.entries['SearchPerLoop'].get()),
            'SleepTime': float(self.view.entries['SleepTime'].get())
        }
        
        self.model.RunBuyAndStore(**InputData)
        

    def UpdateBotStats(self):
        print("New Thread is created for UpdateBotStats ")
        self.view.label['SearchStats'].config(text = "Total search: {}, Total bought: {}, Total missed: {}".format(self.model.SearchedNumbers, 
                                                                                                                    self.model.BoughtPlayers, 
                                                                                                                    self.model.FailToBuyPlayers))
        self.view.label['PortfolioStats'].config(text = "Total coin used: {}".format(self.model.CoinUsed))

    def RunBuyAndStoreClickThread(self):
        thread = threading.Thread(target = self.RunBuyAndStoreClick, daemon=True)
        thread.start()


    def five_seconds(self):
        time.sleep(3)
        self.view.label['Stats'].config(text="{} seconds is up, driver are: {}, {}".format(random.randint(1,10), self.model.BoughtPlayers, self.model.driver))




class CSVInputController(Controller):
    def __init__(self, model:CrocodileTrader) -> None:
        self.model = model
        self.view = None


    def bind(self, view: Form):
        self.view = view
        self.view.CreateCSVInputView()

        self.view.buttons['UploadCSVInput'].configure(command = lambda: threading.Thread(target = self.UploadCSVInput, daemon=True).start())
        self.view.buttons['BuyAndStoreWithCSVInput'].configure(command = lambda: threading.Thread(target = self.BuyAndStoreWithCSVInput, daemon=True).start())


    def UploadCSVInput(self):
        print("New thread is created for BuyAndStore")
        self.filename = filedialog.askopenfilename()



    def BuyAndStoreWithCSVInput(self):
        print("New Thread is created for BuyAndStoreWithCSVInput ")
        InputData= {
            'SetMaxMinBid':1000,
            'SearchPerLoop': int(self.view.entries['SearchPerLoop'].get()),
            'SleepTime': float(self.view.entries['SleepTime'].get())
        }
        InputData['CSVinput'] = self.filename
        while(True):
            self.model.RunBuyAndStoreWithCSVInput(**InputData)
            self.model.SleepGen(45)


class IconSnipeController(Controller):
    def __init__(self, model:CrocodileTrader) -> None:
        self.model = model
        self.view = None
    
    def bind(self, view: Form):
        self.view = view
        self.view.CreateCSVInputView()

        self.view.buttons['UploadCSVInput'].configure(command = lambda: threading.Thread(target = self.UploadCSVInput, daemon=True).start())
        self.view.buttons['BuyAndStoreWithCSVInput'].configure(command = lambda: threading.Thread(target = self.BuyAndStoreWithCSVInput, daemon=True).start())


