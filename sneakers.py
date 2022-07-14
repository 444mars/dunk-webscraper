from dis import show_code
from platform import release
import selectors
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


result = driver.get('https://sneakernews.com/release-dates/')
driver.implicitly_wait(0.5)

#load_more = driver.find_element_by_id("sneaker-release-load-more-btn")


for x in range(20):
    load_more = driver.find_element(by=By.ID, value="sneaker-release-load-more-btn")
    load_more.send_keys("Selenium")
    load_more.click()
    time.sleep(0.1)
    
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
dunks = []
dunks = soup.find_all(string=re.compile("Nike Dunk Low"))

for x in range(len(dunks)):
    print(dunks[x])
    a = dunks[x].parent
    h2 = a.parent
    content_box = h2.parent

    
    release_date = content_box.find('span', class_="release-date")
    if release_date:
        print(release_date.text)
    else:
        print('release date: TBD')

    release_price = content_box.find('span', class_='release-price')
    if release_price:
        print(release_price.text)
    else: 
        print("release price: TBD")

    dunk_data = content_box.find(class_="post-data")
    if dunk_data:
        print(dunk_data.text)
    else:
        print('no data available.')

    print('----------------------------------')


driver.quit()