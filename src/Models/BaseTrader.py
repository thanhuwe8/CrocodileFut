from CrocoUtils.Packages import *

import requests



def telegram_bot_sendtext(bot_message):

    bot_token = '6262150139:AAELkNYIBsjdJ8nOfqD98cS5aEWK04wFmLc'
    bot_chatID = '-1001980912080'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def telegram_bot_sendpic(path):
    bot_token = '6262150139:AAELkNYIBsjdJ8nOfqD98cS5aEWK04wFmLc'
    bot_chatID = '-1001980912080'
    message = ('https://api.telegram.org/bot'+ bot_token + '/sendPhoto?chat_id=' + bot_chatID)
    files = {
    'photo': open(path, 'rb')}
    send = requests.post(message, files=files)




class BaseTrader:
    
    def __init__(self, driver) -> None:
        self.driver = driver
        
        #? setup bot config
        self.bot_config = configparser.ConfigParser(allow_no_value=True)
        self.bot_config.read("./Resources/settings.ini")
        
        #? Bot Stats
        self.SearchedPlayers = 0
        self.BoughtPlayers = 0 
        self.MissedPlayers = 0  
        self.CurrentIteration = 0
        self.CoinHave = 0
        self.CoinUsed = 0
        
        #* Card information
        self.PlayerName = "None"
        self.PlayerPosition = "None"
        self.PlayerRating = "None"
        
        #?
        print(self.bot_config.options('Statistics'))
        
        #? Money spent
    
    def SetController(self, Controller) -> None:
        self.Controller = Controller

    def NotifyControllerBotStats(self):
        self.UpdateLogs()
        self.Controller.UpdateBotStats()

    def getUserConfig(self):
        return(self.bot_config)
    
    def getCoinHave(self):
        CoinHave = self.driver.find_element(
                By.XPATH, '/html/body/main/section/section/div[1]/div[1]/div[1]').text
        CoinHave = str(CoinHave)
        if "," in CoinHave:
            CoinHave = CoinHave.replace(",", "")

        self.CoinHave = int(CoinHave)


    #* Store update information in UpdateLogs
    def UpdateLogs(self):
        """
        Summary: Update the settings.ini file for log to print out to UI
        [BotStats]
        SearchedPlayers = 0
        BoughtPlayers = 0
        MissedPlayers = 0
        CurrentIteration = 0
        CoinHave = 0
        CoinUsed = 0
        PlayerName = 0
        PlayerPosition = 0
        PlayerRating = 0
        """
        
        self.bot_config.read("./Resources/settings.ini")

        try:
            self.bot_config.set("BotStats", "SearchedPlayers",
                            str(self.SearchedPlayers))
            
            self.bot_config.set("BotStats", "BoughtPlayers",
                            str(self.BoughtPlayers))
            
            self.bot_config.set("BotStats", "MissedPlayers",
                            str(self.MissedPlayers))
            
            self.bot_config.set("BotStats", "CurrentIteration",
                            str(self.CurrentIteration))
            
            self.bot_config.set("BotStats", "CoinHave",
                            str(self.CoinHave))
            
            self.bot_config.set("BotStats", "CoinUsed",
                            str(self.BoughtPlayers))
            
            self.bot_config.set("BotStats", "PlayerName",
                            str(self.PlayerName))
            
            self.bot_config.set("BotStats", "PlayerPosition",
                            str(self.PlayerPosition))
            
            self.bot_config.set("BotStats", "PlayerRating",
                            str(self.PlayerRating))
            
            
            with open("./Resources/settings.ini", 'w') as configfile:
                self.bot_config.write(configfile)

        except:
            print("Something wrong with the log file")

    #* THIS SECTION IS FOR MENU INTERACTION
    def GoToHome(self) -> None:
        self.driver.find_element_by_xpath("/html/body/main/section/nav/button[1]").click()
    
    
    #? Go to Transfer from the left "Navigation bar"
    def GoToTransfer(self) -> None:
        self.driver.find_element_by_xpath("/html/body/main/section/nav/button[3]").click()


    #? Go to "Transfer List"
    def GotoTransfersList(self, fromMenu=False) -> None:
        try:
            if fromMenu == False:
                
                self.driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[2]").click()
            else:
                self.driver.find_element_by_xpath("/html/body/main/section/nav/button[3]").click()
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/div[2]')))
                self.driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[2]").click()
        except:
            print('Cannot go to: Transfer List')


    #? Go to "Transfer Targets"
    def GoToTransferTargets(self, fromMenu=False) -> None:
        try: 
            if fromMenu == False:
                self.driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[4]").click()
            else:
                self.driver.find_element_by_xpath("/html/body/main/section/nav/button[3]").click()
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/div[2]')))
                self.driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[4]").click()
        except:
            print('Cannot go to: Transfer Targets')


    #? Go to "Search the transfer market"
    def GoToSearchMarket(self, fromMenu) -> None:
        try: 
            if fromMenu == False:
                self.driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[2]").cick()
            else:
                self.driver.find_element_by_xpath("/html/body/main/section/nav/button[3]").click()
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/div[2]')))
                self.driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[2]").click()
        except:
            print('Cannot go to: Search the Transfer Markets')
    
    
    #* this part is used to manipulate the transfer target
    def ClearSoldItems(self) -> None:
        pass
    
    def ClearExpiredItems(self) -> None:
        try:
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div/section[4]/header/button').click()
        except:
            print("cannot Clear Expired item")
    
    def ScanActiveBids(self) -> None:
        pass

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



    #? This part is used to fill in input in transfer market
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

    def FillNameInput(self, input="Ronaldo", namePosition=1):
        if input:
            driver = self.driver
            driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input').clear()
            driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input').click()
            driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input').send_keys(input)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/ul/button[{}]'.format(namePosition))))
            #! namePosition is used to select which item the bot will choose (Xabi Alonso include 3/4 items when we enter the name to search)
            driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/ul/button[{}]'.format(namePosition)).click()
    
    def FillQualityInput(self, input):
        self.FillOneInput(input=input, divindex=2)
    
    def FillRarityInput(self, input):
        self.FillOneInput(input=input, divindex=3)
    
    def FillPositionInput(self, input):
        self.FillOneInput(input=input, divindex=4)
    
    def FillChemistryInput(self, input):
        self.FillOneInput(input=input, divindex=5)
    
    def FillNationatlityInput(self, input):
        self.FillOneInput(input=input, divindex=6)
    
    def FillLeagueInput(self, input):
        self.FillOneInput(input=input, divindex=7)
    
    def FillClubInput(self, input):
        self.FillOneInput(input=input, divindex=8)


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
        
        #! Action 0: input "NAME"
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
        
        #! Action 6: Choose "club"
        self.FillOneInput(input=club, divindex=8)


    def PrintAllInputValue(self, divindex=2):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{}]'.format(divindex)).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{}]/div'.format(divindex))))
        ListOfInputs = driver.find_elements_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{}]/div/ul/li'.format(divindex))
        for index in range(1, len(ListOfInputs)+1):
            print(driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[{}]/div/ul/li[{}]'.format(divindex,index)).text)

    
    
    
    
    
    
    
    #* ----------------------------------------------------------------------------------------------------------------------------------------------------

    #? This part is used to print out the data from "search the transfer market activities"
    def PrintSearchedPlayer(self):
        all_players = driver.find_elements_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li')
        if len(all_players) == 0:
            print("nothing found, please try again")
        else:
            pass

    
    #? Scan in 1 page the average price available
    def ScanAverageBuyNowPrice(self):
        driver = self.driver
        all_players = driver.find_elements_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li')
        if len(all_players) > 0:
            players_found = len(all_players)
            print('Players found: {}'.format(players_found))
            
            #! INFORMATION FOR LATER STEP
            price_container = []
            name_container = []
            price_sum = 0
            for i in range(1,players_found+1):
                # print(i)
                buy_now_price = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]/div/div[2]/div[3]/span[2]'.format(str(i))).text.replace(',', '')
                price_sum += int(buy_now_price)
                price_container.append(int(buy_now_price))
                
                #! EXTRA INFORMATION
                name = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]/div/div[1]/div[2]'.format(i)).text
                rating = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]/div/div[1]/div[1]/div[5]/div[2]/div[1]'.format(i)).text
                position = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]/div/div[1]/div[1]/div[5]/div[2]/div[2]'.format(i)).text

                name_container.append(name)
                
            average_price = price_sum/len(all_players)
            
            print("average price this page is: {}".format(average_price))
            print("Total player found this page is: {}".format(players_found))
            print("Min price found this page is: {}".format(min(price_container)))
            print("Max price found this page is: {}",format(max(price_container)))
            print("All players found: {}".format(set(name_container)))
            return(average_price)
        else: 
            print("there is no player found, return -1")
            return -1


    #? Scan multiple page instead of 1 page
    #todo: I need a recursion version for this loop
    def ScanAverageBuyNowMultiple(self):
        driver = self.driver
        avg_price = self.ScanAverageBuyNowPrice()
        if avg_price != -1:
            status = True
            counter = 1
            self.SleepGen(1)
            while status:
                try:
                    driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/div/button[2]').click()
                    self.SleepGen(2) #? sleep to make sure the page is loaded properly into Selenium
                    print("Page number {}".format(counter))
                    next_avg_price = self.ScanAverageBuyNowPrice()
                    avg_price = (avg_price + next_avg_price)/2
                    counter +=1 
                except:
                    status = False
            return(avg_price)
        else: 
            return(-1)

    
    #? 
    def ScanSearchedCardInfo(self):
        pass
    



    #* ----------------------------------------------------------------------------------------------------------------------------------------------------

    #? This part is used to perform buy and sell activities on the market
    def SetMinBid(self, BuyPrice, SetMaxMinBid=1000):
        driver = self.driver
        MinBid = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/input").get_attribute('value')
        MinBid = MinBid.replace(",", "")
        print("Min Bid: {}".format(MinBid))
        if MinBid == '':
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/input").send_keys('150')
        elif int(MinBid) <= SetMaxMinBid and int(MinBid) < BuyPrice:
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[2]").click()
        else:
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/input").clear()


    def BuyAndStore(self, BuyPrice=400, SetMaxMinBid=1000, FirstOnly=True):
        driver = self.driver
        global running
        running = True
        
        #! Action 1: set the "Min of BID PRICE":
        self.SetMinBid(BuyPrice=BuyPrice, SetMaxMinBid=SetMaxMinBid)
        
        #! Action 3: CLEAR the "Max of BID PRICE" and "Min of BUY NOW PRICE"
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/input").clear()
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]/input").clear()
        
        #! Action 4: set the "Max of BUY NOW PRICE":
        driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input').clear()
        driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input').send_keys(BuyPrice)
        
        #! Action 5: Click Search
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]").click()
        self.SleepGen(1)
        all_players = driver.find_elements_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li')
        
        #! Update BotStats - 1 attributes
        self.SearchedPlayers += 1

        #! Action 6: Check if there is anything pops up
        if len(all_players) == 0:
            print("Nothing found, re-try!")
            print(len(all_players))
            self.SleepGen(1.5)
            driver.find_element_by_xpath('/html/body/main/section/section/div[1]/button[1]').click()
        else:
            print(len(all_players))
            print("total player found is {}".format(len(all_players)))
            
            # all_counter = len(all_players) + 1
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
                
                #! Update BotStats - 3 attributes
                self.PlayerName = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]/div/div[1]/div[2]'.format(i)).text
                self.PlayerRating = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]/div/div[1]/div[1]/div[5]/div[2]/div[1]'.format(i)).text
                self.PlayerPosition = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]/div/div[1]/div[1]/div[5]/div[2]/div[2]'.format(i)).text
                
                
                if current_coin_wallet > current_buynow:
                    if current_buynow <= BuyPrice:
                        #! BUY SECTION
                        print("Starting to buy")
                        
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
                        
                        #! Save screenshot and send mess to telegram
                        now = datetime.now()
                        current_time = now.strftime("%H_%M_%S")
                        current_time = str(current_time)
                        file_name = current_time + ".png"
                        driver.save_screenshot(r"./Output/{}".format(file_name))
                        
                        saved_path = r"./Output/{}".format(file_name)
                        print(saved_path)
                        try:
                            telegram_bot_sendpic(saved_path)
                        except:
                            print("cannot send info to bot")
                        
                        if 'won' in status:
                            telegram_bot_sendtext("Bought")
                            print("BOUGHT")
                            print("START TO SELL")
                            WebDriverWait(driver, 1.5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[8]')))
                            driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[3]/button[8]').click()
                            
                            #! Update BotStats - 2 attributes
                            self.CoinUsed += current_buynow
                            self.BoughtPlayers += 1
                            
                            #todo: 
                            
                            print("store succesfully")
                            break
                        else:
                            print("Cannot Buy players!")
                            print("Retry")
                            
                            #! Update BotStats - 1 attributes
                            self.MissedPlayers +=1
                            # self.FailToBuyPlayer
                        #! THIS SECTION IS USED TO SEND INFORMATION TO TELEGRAM BOT
                else:
                    print("Dont have enough coin")

                if FirstOnly == True:
                    break
                    

            self.SleepGen(2)
            driver.find_element_by_xpath('/html/body/main/section/section/div[1]/button[1]').click()
            
                            
        #! Update total coin having
        self.getCoinHave()
            
        #! Update log to Update Status in UI
        self.NotifyControllerBotStats()


    def BuyAndSell(self, BuyPrice=400, SellPrice=550, SetMaxMinBid=1000):
        
        global running
        running = True
        
        BuyPrice = BuyPrice - 50 
        
        #! Clear and iterate Min Bid
        self.SetMinBid(self, BuyPrice=BuyPrice, SetMaxMinBid=SetMaxMinBid)
        
        #! Set Buy Now Price
        driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input').clear()
        driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input').send_keys(BuyPrice)
            
        
        #* CLick Search
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]").click()
        self.sleep_gen(1)
        all_players = driver.find_elements_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li')

        #* CHECK IF THERE IS ANYTHING FOUND
        if len(all_players) == 0:
            print("Nothing,retry!") #! write into a log console/log file
            print(len(all_players))
            self.sleepgen(1.5)
            driver.find_element_by_xpath('/html/body/main/section/section/div[1]/button[1]').click()
        else:
            #* IF FOUND PLAYERS:
            print(len(all_players))
            print("player found:") #todo: write into a log console/log file
            
            all_counter = len(all_players)+1
            for i in range(1, len(all_players)+1):
                if running == False:
                    break
                
                #? Click on the item available
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]'.format(i))))
                driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]'.format(i)).click()
                
                #? Scan the current buy now price
                current_buynow = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]/div/div[2]/div[3]/span[2]'.format(i)).text
                current_buynow = int(current_buynow.replace(",", ""))
                
                #? Scan the current coin available from wallet
                current_coin_wallet = driver.find_element_by_xpath("/html/body/main/section/section/div[1]/div[1]/div[1]").text
                current_coin_wallet = current_coin_wallet.replace(",", "")
                current_coin_wallet = int(current_coin_wallet)
                
                #? Important check: coin > current_buynow and current_buynow < BuyPrice, otherwise misclick you buy 10k for 1 gold rare
                if current_coin_wallet > current_buynow:
                    if current_buynow <= BuyPrice: 
                        print("Starting to buy")
                        
                        #! BUY SECTION
                        #! Click Buy now Button
                        driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]').click()
                        print("Pressed Buy Now")
                        
                        #! WAIT FOR POP UP WINDOW
                        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/section/div/div/button[1]/span[1]')))
                        self.sleep_gen(0.3)
                        
                        #! CLICK OK NOW
                        driver.find_element_by_xpath('/html/body/div[4]/section/div/div/button[1]/span[1]').click()
                        self.sleep_gen(1.3)
                        
                        #! NOTIFICATION
                        self.sleep_gen(1)
                        WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]'.format(i))))
                        status = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]'.format(i)).get_attribute('class')
                        print(status)
                        
                        if 'won' in status:
                        #! SELL SECTION
                            print("Buy successfully: {}".format(current_buynow))
                            
                            #! Click "List on Transfer Market"
                            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[1]')))
                            driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[1]').click()
                            
                            #! Wait until price pop up
                            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/button')))
                            
                            #! Send "Starting Price" to sell (min selling price)
                            starting_price = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/input')
                            starting_price.click()
                            starting_price.send_keys(Keys.BACKSPACE)
                            self.sleep_gen(1)
                            starting_price.send_keys(SellPrice)
                            
                            self.sleep_gen(1)
                            print("Start to sell min price: {}".format(SellPrice))
                            
                            #! Send "Buy Now Price" to sell (max selling price)
                            buy_now_price = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/input')
                            buy_now_price.click()
                            buy_now_price.send_keys(Keys.BACKSPACE)
                            self.sleep_gen(1)
                            print("Start to sell max price: {}".format(SellPrice))
                            buy_now_price.send_keys(SellPrice)
                            
                            #! Click "List For Transfer"
                            driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/button').click()
                            
                            #! END OF SELL SECTION
                            print("SELL SUCESSFULLY")
                            break
                        else:
                            print("Cannot Buy Player at {}")
                            print("Retry")
                else:
                    print("Dont have enough coin")
                    
            #! Print Buy and Store data into settings file
            
            self.sleepGen(2)
            driver.find_element_by_xpath('/html/body/main/section/section/div[1]/button[1]').click()


    def RunBuyAndStore(self, BuyPrice=400, SetMaxMinBid=1000, SearchPerLoop=50, SleepTime=3, LongBreak=30, FirstOnly=True):
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
            if i == 1:
                self.CurrentIteration = 0
            else:
                self.CurrentIteration += 1
            # if i % 50 == 0:
            #     self.SleepGen(LongBreak)
            self.BuyAndStore(BuyPrice=BuyPrice, SetMaxMinBid=SetMaxMinBid)
            self.SleepGen(SleepTime)
    

    def RunBuyAndStoreWithCSVInput(self, CSVinput, SetMaxMinBid=1000, SearchPerLoop=50, SleepTime=3, namePosition=1, LongBreak=50):
        while True:
            self.df = pd.read_csv(CSVinput)
            self.df = self.df.replace({np.nan:None})
            IterationList = self.df.to_dict(orient='records')
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
    
    
    
    


    #* ----------------------------------------------------------------------------------------------------------------------------------------------------
    #? This part is most difficult engine in the library which manipulates bidding 
    def AutoBidOne(self, MinBid, MaxBid):
        '''
        This function is use to autobid one target only until the price exceeding maxBid or time out
        '''
        driver = self.driver




if __name__ == "__main__":
    driver = uc.Chrome()
    driver.set_window_size(1500, 1060)
    driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")
    
    # Click on Home
    driver.find_element_by_xpath("/html/body/main/section/nav/button[1]").click()
    
    # Click on Squads
    
    # click on Transfers
    driver.find_element_by_xpath("/html/body/main/section/nav/button[3]").click()
    
    # click on "SEARCH THE TRANSFER MARKET"
    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[2]").click()
    
    
    # Test CrocodileTrader
    test = BaseTrader(driver=driver)
    
    
    test.GoToHome()
    test.GotoTransfersList(fromMenu=True)
    test.GoToSearchMarket(fromMenu=True)
    test.GoToTransferTargets(fromMenu=True)
    
    
    test.ScanAverageBuyNowPrice()
    test.ScanAverageBuyNowMultiple()
    
    
    active_bid = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div/section[1]/ul')
    len(active_bid)
    active_bid_tracking = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div/section[1]/ul/li')
    
    ## time: /html/body/main/section/section/div[2]/div/div/div/section[1]/ul/li/div/div[2]/div[4]/span[2] "<30 Seconds"
    
    
    
    #/html/body/main/section/section/div[2]/div/div/div/section[2]/div[2]
    watched_items = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div/section[2]')
    
    
    won_items = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div/section[3]/ul')
    # first element: /html/body/main/section/section/div[2]/div/div/div/section[3]/ul/li[1]
    
    # Manipulate won items:
    driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div/section[3]/ul/li[1]').click() # Choose won items
    driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[3]/button[8]').click() # Send to transfer list
    
    
    
    
    # all_players = driver.find_elements_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li')
    # i=1
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]'.format(i))))
    
    # driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]'.format(i)).click()
    
    # name = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[4]').text
    
    # attributes = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[7]')
    
    # #/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[7]/div[2]
    # rating  = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[7]/div[2]')
    # # position = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div/div[7]/div[2]/div[2]')
    
    # # 1st item
    # # /html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[1]/div[2]
    # name_from_left = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[1]/div[2]').text
    # rating_from_left = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[1]/div[1]/div[5]/div[2]/div[1]').text
    # position_from_left = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[1]/div[1]/div[5]/div[2]/div[2]').text
    
    
    # stat_from_left = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[1]/div[3]').text
    
    
    # start_price = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[2]/div[1]/span[2]')
    # bid_price = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[2]/div[2]/span[2]').text
    # buy_now_price = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[2]/div[3]/span[2]').text
    # time_left = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[2]/div[4]/span[2]').text
    
    
    # try:
    #     next_button= driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/div/button[2]').click()
    #     WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[1]/div/div/button[2]')))
    
    # def ScanAverageBuyNowPrice():
    #     all_players = driver.find_elements_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li')
    #     if len(all_players) > 0:
    #         players_found = len(all_players)
    #         print('Players found: {}'.format(players_found))
    #         price_container = []
    #         price_sum = 0
    #         for i in range(1,players_found+1):
    #             print(i)
    #             buy_now_price = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]/div/div[2]/div[3]/span[2]'.format(str(i))).text.replace(',', '')
    #             price_sum += int(buy_now_price)
    #             price_container.append(int(buy_now_price))
    #         average_price = price_sum/len(all_players)
    #         print("average price this page is: {}".format(average_price))
    #         return(average_price)
    #     else: 
    #         print("there is no player found, return None")
    #         return -1


    # def ScanAverageBuyNowMultiple():
    #     avg_price = ScanAverageBuyNowPrice()
    #     if avg_price != -1:
    #         status = True
    #         while status:
    #             try:
    #                 driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/div/button[2]').click()
    #                 self.SleepGen
    #                 next_avg_price = ScanAverageBuyNowPrice()
    #                 avg_price = (avg_price + next_avg_price)/2
    #             except:
    #                 status = False
    #         return(avg_price)
    #     else: 
    #         return(-1)
            
    
    
    
    
    # ScanAverageBuyNowMultiple()
    