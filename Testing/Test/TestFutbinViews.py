
from Views.QuickSnipeView import *
from Models.BaseTrader import *





class SnipeController():

    def __init__(self, model, view) -> None:
        
        self.model = model
        self.view = view
        # self.view.buttons['RunBuyAndStore'].configure(command= lambda: threading.Thread(target = self.five_seconds, daemon=True).start())
        self.view.StartSnipeButton.configure(command = lambda: threading.Thread(target = self.RunBuyAndStoreClick, daemon=True).start())
        # self.view.buttons['UpdateBotStats'].configure(command = lambda: threading.Thread(target = self.UpdateBotStats, daemon=True).start())


    def RunBuyAndStoreClick(self):
        print("New thread is created for BuyAndStore")
        
        InputData= {
            'BuyPrice': float(self.view.BuyPriceEntry.get()),
            'SearchPerLoop': int(self.view.SearchPerLoop.get()),
            'SleepTime': float(self.view.GapTimeEntry.get()),
            'LongBreak': float(self.view.LongBreakEntry.get())
        }
        
        self.model.RunBuyAndStore(**InputData)






if __name__ == "__main__":
    
    driver = uc.Chrome()
    # driver.get("https://www.futbin.com/")
    driver.set_window_size(1200, 900)
    driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")

    #! create model
    Engine = BaseTrader(driver)

    #! Create root
    root = tb.Window(themename='minty')
    root.title("Crocodile Fut Trading")
    root.geometry('400x600')



    #! create view
    SnipeView = QuickSnipeView(root,bootstyle="minty")
    SnipeView.grid(row=0,column=0)
    SnipeView.columnconfigure(0,weight=1)
    SnipeView.rowconfigure(0,weight=1)


    Controller = SnipeController(model=Engine, view=SnipeView)
    root.mainloop()










