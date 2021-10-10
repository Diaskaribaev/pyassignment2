# Web Scrapping tool for Cryptocurrencies


### Installation
PyPi 
```bash
pip install bs4
pip install BeautifulSoup
pip install requests
```
### Usage

```python
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from rich import print
```

### Examples
```python
>>>coin=input() #here you input name of cryptocurencies 
>>>url = 'https://coinmarketcap.com/currencies/' + str(coin) +'/news/'#it is a url link which will show you articles about crypticuruncies 
>>>driver = webdriver.Firefox()
#The driver.get method will navigate to a page given by the URL. WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired) before #returning control to your test or script.
>>>driver.get(url)

>>>page = driver.page_source
>>>page_soup = soup(page,'html.parser')#BeautifulSoup object, which represents the document as a nested data structure


>>>data=''
>>>for data in page_soup.find_all("p"): 
    print(data.get_text()) #shows text which in <p> tag
>>>output
With the Lightning Network hitting a capacity of 3,000 BTC, crypto influencers have been talking a lot about a hypothetical Bitcoin standard &#8211; and what 
the transition to such a world could look like. During an episode of the What Bitcoin Did podcast in Nashville, Tennessee,...
October, the 4th quarter of the year, is giving Bitcoiners multiple reasons to stay bullish. To start with, Bitcoin bulls seem to be leaving no room for delayas they have began to warm up immediately after the new month hit. The bulls are already attempting $60,000 as analysts n...
The Junior Senator from the ‘Equality State’ is a strong advocate of crypto and bitcoin.
Bitcoin (BTC/USD) continued to remain rangebound early in the North American session as the pair attracted strong two-way trading activity above the 54000    
figure after recently peaking around the 56113 level, its strongest print following its acute decline in May.&nbsp; This rece...
The Ethereum creator railed that Nayib Bukele "loves being praised" and said "shame on Bitcoin maximalists who are uncritically praising him."




```

## License
[MIT](https://choosealicense.com/licenses/mit/)
