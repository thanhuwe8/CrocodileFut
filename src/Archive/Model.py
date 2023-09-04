from datetime import datetime
from datetime import date
from mimetypes import init
from time import sleep
import random
import warnings
import math

warnings.filterwarnings("ignore", category=DeprecationWarning) 

import keyboard
from threading import Thread
import logging


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


from webdriver_manager.chrome import ChromeDriverManager
#from fake_useragent import UserAgent
import undetected_chromedriver as uc # only need this

import numpy as np
import pandas as pd


def SleepGen(seconds):
    """
    Randomizes sleep to avoid detection.
    """
    upperbound = (seconds+0.2)*10000
    if (seconds >= 1):
        lowerbound = (seconds-0.2)*10000
    else:
        lowerbound = seconds*10000

    sleeptime = random.randint(lowerbound, upperbound)
    sleeptime = sleeptime/10000
    sleeptime = sleeptime*.8

    sleep(sleeptime)


class CrocodileTrader:
    
    def __init__(self, driver) -> None:
        self.driver = driver
        
        #? Stats variable
        self.SearchedNumbers = 0
        self.BoughtPlayers = 0
        self.FailToBuyPlayers = 0
        
        #? Money spent
        self.CoinUsed = 0
    
    
    def SleepGen(self, seconds):
        """
        Randomizes sleep to avoid detection.
        """
        upperbound = (seconds+0.2)*10000
        if (seconds >= 1):
            lowerbound = (seconds-0.2)*10000
        else:
            lowerbound = seconds*10000

        sleeptime = random.randint(lowerbound, upperbound)
        sleeptime = sleeptime/10000
        sleeptime = sleeptime*.8

        sleep(sleeptime)
    
    #! write function for log
    

    
    def FillOneInput(self, input=None, divindex=2):
        """_summary_
        Fill the acccordingly input
        Args:
            input (_type_, optional): _description_. Defaults to None, 
                - value representing input value (for instance, GOLD, RARE, CF, CB, Arsenal etc.)

            divindex (int, optional): _description_. Defaults to 2.
                - 1: Type Player Name
                - 2: QUALITY
                - 3: RARITY
                - 4: POSITION
                - 5: CHEMISTRY STYLE
                - 6: NATIONALITY
                - 7: LEAGUE
                - 8: CLUB
        """        
        driver = self.driver
        if input:
            #? click on "QUALITY" ENTRY
            driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{}]'.format(divindex)).click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{}]/div'.format(divindex))))
            
            #? find relevant "QUALITY" of the pop up list and click
            ListOfInputs = driver.find_elements_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{}]/div/ul/li'.format(divindex))
            for index in range(1, len(ListOfInputs)+1):
                QualityValue = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{}]/div/ul/li[{}]'.format(divindex,index)).text
                if QualityValue == input:
                    driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{}]/div/ul/li[{}]'.format(divindex,index)).click()
                    break
            self.SleepGen(0.6)


    def PrintAllInputValue(self, divindex=2):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{}]'.format(divindex)).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{}]/div'.format(divindex))))
        ListOfInputs = driver.find_elements_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{}]/div/ul/li'.format(divindex))
        for index in range(1, len(ListOfInputs)+1):
            print(driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{}]/div/ul/li[{}]'.format(divindex,index)).text)
    
    
    def FillNameInput(self, input="Ronaldo", namePosition=1):
        if input:
            driver = self.driver
            driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input').clear()
            driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input').click()
            driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input').send_keys(input)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/ul/button[{}]'.format(namePosition))))
            #! namePosition is used to select which item the bot will choose (Xabi Alonso include 3/4 items when we enter the name to search)
            driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/ul/button[{}]'.format(namePosition)).click()


    def FillAllInputs(self, name=None, quality=None, rarity=None, position=None, chemistry=None, nationality=None, league=None, club=None, namePosition=1):
        
        driver = self.driver
        #? click on the transfer item on left navigation panel
        driver.find_element_by_xpath("/html/body/main/section/nav/button[3]").click() 
        
        
        #? wait for a while, then click on "SEARCH THE TRANSFER MARKET"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/div[2]')))
        driver.find_element_by_xpath("//html/body/main/section/section/div[2]/div/div/div[2]").click()
        self.SleepGen(1)
        
        #? click reset button
        driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[1]').click()
        
        #! Action 0: input "Name"
        self.FillNameInput(input=name, namePosition=namePosition)
        
        #! Action 1: Choose "QUALITY"
        self.FillOneInput(input=quality, divindex=2)

        #! Action 2: Choose "RARITY"
        self.FillOneInput(input=rarity, divindex=3)

        #! Action 3: Choose "POSITION"
        self.FillOneInput(input=position, divindex=4)

        #! Action 4: Choose "CHEMISTRY"
        self.FillOneInput(input=chemistry, divindex=5)
        
        #! Action 5: Choose "NATIONALITY"
        self.FillOneInput(input=nationality, divindex=6)
        
        #! Action 5: Choose "LEAGUE"
        self.FillOneInput(input=league, divindex=7)
        
        #! Action 5: Choose "LEAGUE"
        self.FillOneInput(input=club, divindex=8)


    def BuyAndStore(self, BuyPrice=400, SetMaxMinBid=1000):
        driver = self.driver
        global running
        running = True
        
        #! Action 1: set the "Min of BID PRICE":
        MinBid = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/input").get_attribute('value')
        MinBid = MinBid.replace(",", "")
        print("CURRENT MIN BID PRICE IS: {}".format(MinBid))
        if MinBid == '':
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/input").send_keys('150')
        elif int(MinBid) < SetMaxMinBid and int(MinBid) < BuyPrice:
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[2]").click()
        else:
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/input").clear()
        
        #! Action 3: CLEAR the "Max of BID PRICE" and "Min of BUY NOW PRICE"
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/input").clear()
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]/input").clear()
        
        #! Action 4: set the "Max of BUY NOW PRICE":
        driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input').clear()
        driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input').send_keys(BuyPrice)
        
        #! Action 5: Click Search
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]").click()
        self.SearchedNumbers += 1
        self.SleepGen(1)
        all_players = driver.find_elements_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li')

        #! Action 6: Check if there is anything pops up
        if len(all_players) == 0:
            print("Nothing found, re-try!")
            print(len(all_players))
            self.SleepGen(1.5)
            driver.find_element_by_xpath('/html/body/main/section/section/div[1]/button[1]').click()
        else:
            print(len(all_players))
            print("total player found is {}".format(len(all_players)))
            
            all_counter = len(all_players) + 1
            for i in range(1, len(all_players)+1):
                if running == False:
                    break
                
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]'.format(i))))
                driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]'.format(i)).click()
                
                current_buynow = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]/div/div[2]/div[3]/span[2]'.format(i)).text
                current_buynow = int(current_buynow.replace(",", ""))
                
                current_coin_wallet = driver.find_element_by_xpath("/html/body/main/section/section/div[1]/div[1]/div[1]").text
                current_coin_wallet = current_coin_wallet.replace(",", "")
                current_coin_wallet = int(current_coin_wallet)
                
                if current_coin_wallet > current_buynow:
                    if current_buynow <= BuyPrice:
                        print("Starting to buy")
                        #! BUY SECTION
                        #! Click Buy now Button
                        print(i)
                        print("STARTING TO BUY")
                        driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]').click()
                        
                        #! WAIT FOR POP UP WINDOW
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/section/div/div/button[1]/span[1]')))
                        self.SleepGen(0.3)
                        #! CLICK OK NOW
                        driver.find_element_by_xpath('/html/body/div[4]/section/div/div/button[1]/span[1]').click()
                        self.SleepGen(1.3)
                        
                        #! NOTIFICATION
                        self.SleepGen(1)
                        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]'.format(i))))
                        status = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]'.format(i)).get_attribute('class')
                        print(status)
                        
                        #! Save screenshot
                        now = datetime.now()
                        current_time = now.strftime("%H_%M_%S")
                        current_time = str(current_time)
                        path = current_time + ".png"
                        driver.save_screenshot(path)
                        
                        if 'won' in status:
                            self.CoinUsed += current_buynow
                        #! SELL SECTION
                            print("Buy successfully")
                            print("STARTING TO SELL")
                            #! Click SEND TO TRANSFER LIST
                            WebDriverWait(driver, 1.5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[8]')))
                            driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[8]').click()
                            
                            print("store succesfully")
                            self.BoughtPlayers += 1
                            break
                        else:
                            print("Cannot Buy players!")
                            print("Retry")
                            self.FailToBuyPlayers += 1
                else:
                    print("Dont have enough coin")
            self.SleepGen(2)
            driver.find_element_by_xpath('/html/body/main/section/section/div[1]/button[1]').click()


    def RunBuyAndStore(self, BuyPrice=400, SetMaxMinBid=1000, SearchPerLoop=50, SleepTime=3, LongBreak=30):
        while True:
            for i in range(1, SearchPerLoop):
                print("Iteration number {}".format(i))
                if i == 50 or i == 150 or i == 100:
                    self.SleepGen(20)
                self.BuyAndStore(BuyPrice=BuyPrice, SetMaxMinBid=1000)
                self.SleepGen(SleepTime)
            self.SleepGen(LongBreak)


    def RunBuyAndStoreWithInput(self, BuyPrice=400, SetMaxMinBid=1000, SearchPerLoop=50, SleepTime=3, *args, **kwargs):
        self.FillAllInputs(**kwargs)
        for i in range(1, SearchPerLoop):
            if i % 50 == 0:
                self.SleepGen(20)
            self.BuyAndStore(BuyPrice=BuyPrice, SetMaxMinBid=SetMaxMinBid)
            self.SleepGen(SleepTime)


    def RunBuyAndStoreWithCSVInput(self, CSVinput, SetMaxMinBid=1000, SearchPerLoop=50, SleepTime=3, namePosition=1, LongBreak=50):
        self.df = pd.read_csv(CSVinput)
        self.df = self.df.replace({np.nan:None})
        IterationList = self.df.to_dict(orient='records')
        while True:
            for i in range(len(IterationList)):
                print("Input Element Number {}".format(i))
                DictInput = IterationList[i]
                DictInput['namePosition'] = namePosition
                print(DictInput)
                SetBuyPrice = DictInput['BuyPrice']
                del DictInput['BuyPrice']
                try:
                    del DictInput['SellPrice']
                except KeyError:
                    pass
                FilterInput = DictInput
                self.FillAllInputs(**FilterInput)
                for j in range(1, SearchPerLoop):
                    print("Iteration for this entry: {}".format(j))
                    if j % 50 == 0:
                        self.SleepGen(20)
                    self.BuyAndStore(BuyPrice=SetBuyPrice, SetMaxMinBid=SetMaxMinBid)
                    self.SleepGen(SleepTime)
            self.SleepGen(LongBreak)
    
    
    def ScanMarketSinglePlayer(self, PriceGuess, PriceIncremental, *args, **kwargs):
        driver = self.driver
        self.FillAllInputs(**kwargs)
        
        self.keepsearching = True
        self.SearchDirection = "Higher"
        self.CurrentMarketPrice = PriceGuess
        self.Found = False
        
        while(self.keepsearching):
            #! Input the PriceGuess
            driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input').clear()
            driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input').send_keys(PriceGuess)
            
            
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]").click()
            self.SleepGen(1)
            all_players = driver.find_elements_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li')
            
            
            if len(all_players) == 0:
                if self.Found == True:
                    self.keepsearching = False
                    self.FairPrice = self.CurrentMarketPrice
                else:
                    print("Nothing found, re-try!")
                    self.SleepGen(1)
                    self.SearchDirection = "Higher"
                    self.CurrentMarketPrice += PriceIncremental
                    driver.find_element_by_xpath('/html/body/main/section/section/div[1]/button[1]').click()
            else:
                if self.Found == True:
                    if self.SearchDirection == "Higher":
                        self.keepsearching = False
                        self.FairPrice = self.CurrentMarketPrice
                    else:
                        self.keepsearching = True
                        self.CurrentMarketPrice -= PriceIncremental
                        self.SearchDirection = "Lower"
                    driver.find_element_by_xpath('/html/body/main/section/section/div[1]/button[1]').click()
                else:
                    self.Found = True
                    self.SearchDirection = "Lower"
                    self.keepsearching = True


    def WaitForShieldInvisibility(self, duration=0.25):
        WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located(
            (By.CLASS_NAME, 'ut-click-shield showing interaction'))
        )


    def GotoMenuTransfers(self):
        try:
            #? Click on the 
            self.driver.find_element(By.CLASS_NAME, 'icon-transfer').click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, 'ut-tile-transfer-market'))
            )
            self.SleepGen(0.6)
            print("Go to 'Transfers' successfully")
        except:
            print("Cannot open 'Transfers'")
    
    
    def GotoTransferMarket(self):
        self.GotoMenuTransfers()
        self.driver.find_element(
                By.CLASS_NAME, 'ut-tile-transfer-market').click()
        self.SleepGen(0.6)


    def GotoWatchlist(self):
        self.GotoMenuTransfers()
        self.driver.find_element(
                By.CLASS_NAME, 'ut-tile-transfer-targets').click()
        self.SleepGen(0.6)


    def UpdateTradingStatus(self):
        self.GotoMenuTransfers()
        
        #? Transfer list section
        self.selling_tracker = int(self.TextFromxpath('/html/body/main/section/section/div[2]/div/div/div[3]/div[2]/div/div[2]/span[2]'))
        print(self.selling_tracker)
        
        self.sold_tracker = int(self.TextFromxpath('/html/body/main/section/section/div[2]/div/div/div[3]/div[2]/div/div[3]/span[2]'))
        print(self.sold_tracker)
        
        #? Watchlist section
        self.winning_tracker = int(self.TextFromxpath('/html/body/main/section/section/div[2]/div/div/div[4]/div[2]/div/div[2]/span[2]'))
        print(self.winning_tracker)
        
        self.outbid_tracker = int(self.TextFromxpath('/html/body/main/section/section/div[2]/div/div/div[4]/div[2]/div/div[3]/span[2]'))
        print(self.outbid_tracker)


    def GetPlayersInfo(self, sleeptime=1):
        self.SleepGen(sleeptime)
        
        # status = self.checkWebAppStatus("TransferMarket")
        PlayersList = self.driver.find_elements(By.TAG_NAME, 'listFUTItem')        
    
    
    def GetPlayersBidStatus(self, OrderIdx):
        CurrentCard =  self.driver.fin_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]".format(OrderIdx))
        BidStatus = str(CurrentCard.get_attribute("Class"))
        return(BidStatus)




    
    # Utilities functions
    def TextFromxpath(self, xpath):
        item = self.driver.find_element(By.XPATH, xpath)
        text_value = item.text
        
        if len(text_value) == 0:
            text = item.get_attribute("innerHTML")
            return(text)
        else:
            return text_value



    def WaitVisibilityXpath(self, xpath):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, xpath))
        )




