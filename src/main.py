from Views.QuickSnipeView import *
from Controllers.SnipeController import *

from Models.BaseTrader import *
from Models.BidWarTrader import *



if __name__ == "__main__":
    
    # driver = uc.Chrome()
    # driver.get("https://www.futbin.com/")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")       
    
    driver.set_window_size(1600, 1200)
    driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")

    #! create model
    # Crocodile = BaseTrader(driver)
    Crocodile = BidWarTrader(driver)

    #! Create root
    root = tb.Window(themename='solar')
    root.title("Crocodile Fut Trading")
    root.iconbitmap("main.ico")
    root.geometry('800x800+500+500')


    #! create view
    SnipeView = QuickSnipeView(root,bootstyle="minty")
    SnipeView.grid(row=0,column=0)
    SnipeView.columnconfigure(0,weight=1)
    SnipeView.rowconfigure(0,weight=1)


    Controller = SnipeController(model=Crocodile, view=SnipeView)
    
    # ! Make Controller observer for the bot
    Crocodile.SetController(Controller)
    
    
    root.mainloop()









