from bs4 import BeautifulSoup as soup
from selenium import webdriver
from rich import print

coin=input()
url = 'https://coinmarketcap.com/currencies/' + str(coin) +'/news/'
driver = webdriver.Firefox()
driver.get(url)

page = driver.page_source
page_soup = soup(page,'html.parser')


data=''
for data in page_soup.find_all("p"): 
    print(data.get_text()) 