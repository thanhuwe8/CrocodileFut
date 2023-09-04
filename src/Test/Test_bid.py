

############################################ TESTING SECTION ############################################
driver = uc.Chrome()
# driver.get("https://www.futbin.com/")
driver.set_window_size(1500, 1060)
driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")




a = CrocodileTrader(driver=driver)
a.GotoTransferMarket()
a.GotoMenuTransfers()
a.UpdateTradingStatus()


CardList = driver.find_elements(By.TAG_NAME, "li.listFUTItem")

playerdata = []

playernumber = 1

for card in CardList:
    BidStatus = card.get_attribute("class")
    PlayerAttributes = card.text.splitlines()
    
    rating = PlayerAttributes[0]
    position = PlayerAttributes[1]
    name = PlayerAttributes[2]
    
    pace = int(PlayerAttributes[4])
    shoot = int(PlayerAttributes[6])
    passing = int(PlayerAttributes[8])
    dribbling = int(PlayerAttributes[8])
    defending = int(PlayerAttributes[12])
    physical = int(PlayerAttributes[14])
    
    startprice = PlayerAttributes[16]
    bidprice = PlayerAttributes[18]
    buynow = PlayerAttributes[20]
    time = PlayerAttributes[22]
    
    
    #! clean price format
    if "," in startprice: startprice = int(startprice.replace(",", ""))
    if "," in buynow: buynow = int(buynow.replace(",", ""))
    
    if "---" in bidprice:
        bidprice = startprice
    elif "," in bidprice:
        bidprice = int(bidprice.replace(",", ""))
    
    
    #? clean time format
    seconds = 0
    if "<" in timeleft:
        if "<5" in timeleft:
            seconds = 5
        elif "<10" in timeleft:
            seconds = 10
        elif "<15" in timeleft:
            seconds = 15
        elif "<30" in timeleft:
            seconds = 30
        elif "Minute" in timeleft:
            seconds = 60
    elif "1 Minute" in timeleft:
        seconds = 60
    elif "Minutes" in timeleft:
        timeleft = timeleft[:-8]
        timeleft = int(timeleft)
        timeleft = 60*timeleft
        seconds = timeleft
    elif "Expired" in timeleft:
        seconds = -5
    elif "Processing" in timeleft:
        seconds = -5
    else:
        seconds = 60*65
    

CardList[0].get_attribute("class")

CardList[1].text.splitlines()
CardList[0]
CardList[0]

CardList[0]


CurrentCard =  driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[{}]".format(2))




CurrentStatus =  driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div/div/section[1]/ul/li[1]")
CurrentStatus.get_attribute("class")




#! Start from here
CurrentCard = driver.find_elements(By.XPATH, "/html/body/main/section/section/div[2]/div/div/div/section[1]/ul/li")

MaxBidAllowed = 15000
new_bidprice = 17000


for i, value in enumerate(CurrentCard):
    print(i)
    CardInfo = driver.find_element(By.XPATH, "/html/body/main/section/section/div[2]/div/div/div/section[1]/ul/li[{}]".format(i+1))
    PlayerAttributes = CardInfo.text.splitlines()
    
    startprice = PlayerAttributes[16]
    bidprice = PlayerAttributes[18]
    buynow = PlayerAttributes[20]
    time = PlayerAttributes[22]


    #! clean price format
    if "," in startprice: startprice = int(startprice.replace(",", ""))
    if "," in buynow: buynow = int(buynow.replace(",", ""))
    
    if "---" in bidprice:
        bidprice = startprice
    elif "," in bidprice:
        bidprice = int(bidprice.replace(",", ""))
    
    BidStatusText = CardInfo.get_attribute('class')
    if "outbid" in BidStatusText:
        print("Current Card is being outbid, current bid price is : {}".format(bidprice))
        if bidprice < MaxBidAllowed:
            if bidprice < 1000:
                new_bidprice = bidprice + 50
            elif bidprice < 10000:
                new_bidprice = bidprice + 100
            else:
                new_bidprice = bidprice + 250
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div/input").click()
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/div/input").send_keys(new_bidprice)
            driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section/div/div/div[2]/div[2]/button[1]").click()

    elif "highest-bid" in BidStatusText:
        print("Current Card is sitting on highest bid, current bid price is : {}".format(bidprice))


#! Check win items:
wonlist = driver.find_elements_by_xpath('/html/body/main/section/section/div[2]/div/div/div/section[3]/ul/li')

#! Create unique key to look up value from bid

#! scroll down


def HelpMeToBid(MaxBidAllowed=300):
    driver = 