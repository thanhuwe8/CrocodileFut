from Models.BaseTrader import *
from CrocoUtils.Constants import USER_AGENTS
from selenium.webdriver import ActionChains

class BidWarTrader(BaseTrader):
    
    def __init__(self, driver) -> None:
        super().__init__(driver)
    
    def BidClick(self):
        pass
    

    
    #! Transfer Target Operation
    def TTTrackBidStatus(self, index=1):
        """_summary_
        return the current status of the bidding war. 3 options as below:
        
        'listFUTItem has-auction-data highest-bid selected'
        'listFUTItem has-auction-data selected outbid'

        Args:
            index (int, optional): _description_. Defaults to 1.
        """        
        status = self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div/section[1]/ul/li').get_attribute('class')
        return(status)

    def TTGetCurrentBid(self, index=1):
        BidPrice = self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]/div/div[2]/div[2]/span[2]'.format(index)).text
        return(BidPrice)


    #! Transfermarket operation
    def TMGetStartPrice(self, index=1):
        StartPrice = self.driver.find_element_by_xpath(r'/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[2]/div[1]/span[2]'.format(index)).text
        return(int(StartPrice.replace(',', '')))
    
    def TMGetCurrentBid(self, index=1):
        CurrentBid = self.driver.find_element_by_xpath(r'/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]/div/div[2]/div[2]/span[2]'.format(index)).text
        if CurrentBid != '---':
            CurrentBid = int(CurrentBid.replace(',', ''))
        return(CurrentBid)
    
    def TMGetCurrentBuyNow(self, index=1):
        CurrentBuyNow = self.driver.find_element_by_xpath(r'/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]/div/div[2]/div[3]/span[2]'.format(index)).text
        return(int(CurrentBuyNow.replace(',', '')))
    
    def TMGetCurrentTime(self, index=1):
        """_summary_
        Args:
            '<15 Seconds'
            '<30 Seconds'
            '<1 Minute'
            
        """        
        CurrentTime = self.driver.find_element_by_xpath(r'/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]/div/div[2]/div[4]/span[2]'.format(index)).text
        return(CurrentTime)
    
    
    def TMPressOnCard(self, index=1):
        try: 
            self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]'.format(index)).click()
        except:
            print("Shit")
    
    def TMModifyBidPrice(self, BidPrice):
        BidPriceModifier = self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div/input')
        self.SleepGen(1.0)
        BidPriceModifier.click()
        MyHand = ActionChains(self.driver)
        MyHand.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
        BidPriceModifier.send_keys(Keys.BACKSPACE)
        
        
        BidPriceModifier.send_keys(BidPrice)
    
    def TMClickMakeBid(self):
        self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[1]').click()
    
    def TMCurrentStatus(self, index=1):
        '''
        listFUTItem has-auction-data selected won
        
        '''
        Status = self.driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]'.format(index)).get_attribute('class')
        return(Status)

    def SearchGetBid(self, BidCycle=5, BidPrice=850, MaxBid = 900, listmax=5):
        
        driver = self.driver
        
        
        BidTracker = 0 
        
        while BidTracker <= BidCycle:
            
            
            #! Action 1: Set the "Min of BID PRICE":
            # self.SetMinBid(BuyPrice=BidPrice, SetMaxMinBid=BidPrice-50)
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/input").clear()
            bid_min_random = random.randint(100,900)
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/input").send_keys(bid_min_random)
            
            #! Action 2: CLEAR the "Max of BID PRICE" our "BidPrice"
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/input").clear()
            driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/input').send_keys(BidPrice)
            
            #! Action 3: CLEAR the "BUY NOW PRICE"
            # driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]/input").clear()
            
            #! Action 4: Click the Search Key
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]").click()
            self.SleepGen(1)
            print("DONE ACTION 4")
            
            #! Action 5: Check how many players are available and press Bid 
            AllPlayers = driver.find_elements_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li')
            print(len(AllPlayers))
            self.SleepGen(0.5)
            
            if len(AllPlayers) == 0:
                print("Nothing found, re-try!")
                print(len(AllPlayers))
                self.SleepGen(0.5)
                driver.find_element_by_xpath('/html/body/main/section/section/div[1]/button[1]').click()
            else:
                print("Players Found {}".format(len(AllPlayers)))
                for i in range(1, len(AllPlayers)+1):
                    if i > listmax: 
                        break
                    try:
                        #? Click on the player card in the list
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]'.format(i))))
                        driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]'.format(i)).click()
                        self.SleepGen(1)
                        
                        #? Check current "BID"
                        CurrentBid = self.TMGetCurrentBid(index=i)
                        
                        if CurrentBid == "---" or CurrentBid < BidPrice:
                            self.TMModifyBidPrice(BidPrice)
                            self.SleepGen(1)
                            # current_input = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div/input').text
                            #! super important
                            input_block = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div/input')
                            input_block.click()
                            MyHand = ActionChains(self.driver)
                            MyHand.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
                            input_number = int(driver.execute_script("return window.getSelection().toString()").replace(',',''))
                            print(input_number)
                            self.SleepGen(0.5)
                            if input_number <= BidPrice:
                                self.TMClickMakeBid()
                            else:
                                print("Something wrong with input, value is too large: {}".format(input_number))
                            self.SleepGen(0.5)
                            
                            BidStatus = self.TMCurrentStatus()
                            if "won" in BidStatus or "highest":
                                print("Bid ok")
                            else:
                                print("Bid not ok")
                        else:
                            print("Bid is higher than the bid expected {} vs {} ".format(BidPrice, CurrentBid))
                            self.SleepGen(1.0)
                    except:
                        print("something is wrong, keep going")
                        break
                #     if self.getCoinHave() < BidPrice:
                #         break
                # if self.getCoinHave() < BidPrice:
                #     break
            BidTracker += 1
            self.SleepGen(2)
            driver.find_element_by_xpath('/html/body/main/section/section/div[1]/button[1]').click()



# driver = webdriver.Chrome(ChromeDriverManager().install())

# driver.set_window_size(1250, 1150)
# driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")


# test = BidWarTrader(driver=driver)
# test.SearchGetBid(20,700,800,7)

# test.SearchGetBid(20,16000,800,7)

# test.BuyAndStore(18000,1000,True)

# # bidPrice = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div/input')
# # bidPrice.click()

# a = driver.execute_script("return window.getSelection().toString()")


# a = test.getCoinHave()