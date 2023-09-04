
# start_price = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[2]/div[1]/span[2]')
# bid_price = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[2]/div[2]/span[2]').text
# buy_now_price = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[2]/div[3]/span[2]').text
# time_left = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/section[1]/div/ul/li[1]/div/div[2]/div[4]/span[2]').text
TimeLeft = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div/section[1]/ul/li[1]/div/div[2]/div[4]/span[2]').text

# '<15 Seconds'
# '<30 Seconds'

#! Transfer target - Active Bids
Name = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div/section[1]/ul/li/div/div[2]/div[1]/span[2]')

StartPrice = int(driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div/section[1]/ul/li/div/div[2]/div[1]/span[2]').text.replace(',',''))
BidPrice = int(driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div/section[1]/ul/li/div/div[2]/div[2]/span[2]').text.replace(',',''))
BuyNowPrice = int(driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div/section[1]/ul/li/div/div[2]/div[3]/span[2]').text.replace(',',''))


status = driver.find_element_by_xpath('/html/body/main/section/section/div[2]/div/div/div/section[1]/ul/li').get_attribute('class')




driver = uc.Chrome(version_main=112)
driver.set_window_size(1500, 1060)
driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")
driver.add_argument()

#! 
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={USER_AGENTS[5]}')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
# driver.get("https://www.ea.com/fifa/ultimate-team/web-app/")
driver.get("https://www.futbin.com/stc/cheapest")
driver.find_element


Test = BidWarTrader(driver=driver)





import requests
from bs4 import BeautifulSoup

HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
url = "https://www.futbin.com/stc/cheapest/"
page = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(page.content, "html.parser")
print(page.prettify())



import requests

headers = {
    ':authority': "https://www.futbin.com/stc/cheapest/",
    ':method': 'GET',
    ':path': '/matches',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'MatchFilter={%22active%22:false%2C%22live%22:false%2C%22stars%22:1%2C%22lan%22:false%2C%22teams%22:[]}',
    'dnt': '1',
    'pragma': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
response = requests.get(url, headers=headers)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)


r = requests.get('https://www.futbin.com/stc/cheapest/', headers=HEADERS)
print(r.text)


url = 'https://www.futbin.com/stc/cheapest'
headers = {'User-Agent': 'Mozilla/5.0'}
cookies = {'platform': 'pc', 'platform_type': 'pc'}

html = requests.get(url, headers=headers, cookies=cookies)

url = 'https://www.futbin.com/23/players?page=1&player_rating=82-82'

headers = {'User-Agent': 'Mozilla/5.0'}
cookies = {'platform': 'pc', 'platform_type': 'pc'}
html = requests.get(url, headers=headers, cookies=cookies).content


soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())


from urllib.request import Request, urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from lxml import etree


url = 'https://www.futbin.com/stc/cheapest'
headers = {'User-Agent': 'Mozilla/5.0'}
req = Request(url, headers=headers)
response = urlopen(req)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())


soup.find_all('d-flex row col-md-9 px-0')

a = soup.find('/html/body/div[9]/div[3]/div[2]/div/div[2]')
dom = etree.HTML(str(soup))
dom.xpath('/html/body/div[9]/div[3]/div[2]/div/div[2]')



HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
}




mydivs = soup.find_all("div", {"class": "d-flex row col-md-9 px-0"})

#! This div is the HTML for each rating group (81 to 95)
mydivs = soup.find_all("div", {"class": "top-stc-players-box"})

print(mydivs[0].find_all("span", {"class":"price-holder-row"}))

name = mydivs[0].find_all("div", {"class":"name-holder"})
name[0].text.replace(" ", "").replace("\n", '')

len(mydivs)

x = mydivs[0].find_all("span", {"class":"price-holder-row"})
type(x)
type(x[0])
x[0].cla
z = x[0].span

int(z.text)

a = pd.read_html(mydivs)

r = requests.get(url, headers=HEADERS)


rating_group = mydivs[0].find("span", {"style":"position: relative; top: 2px;"})
int(rating_group.text.split('\n')[1])
 to 


x = mydivs[0].find_all("span", {"class":"price-holder-row"})


name_container = []
price_container = []

rating_group = int(rating_group.text.split('\n')[1])

name = mydivs[0].find_all("div", {"class":"name-holder"})
price = mydivs[0].find_all("span", {"class":"price-holder-row"})
for i in range(len(name)):
    print(i)
    ThisName = name[i].text.replace(" ", "").replace("\n", '')
    name_container.append(ThisName)
    ThisPrice = int(price[i].text.replace('\n', ''))
    price_container.append(ThisPrice)
    print("{} : {}".format(ThisName, ThisPrice))
    