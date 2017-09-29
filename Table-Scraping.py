import requests
from lxml import html
import bs4 as bs
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    url1 = "https://learn.illinois.edu/"
    url2 = "https://learn.illinois.edu/auth/shibboleth/index.php"
    url3 = "https://wiki.illinois.edu/wiki/display/ece120/Home"
    
    source = urllib.request.urlopen(url3).read()
    soup = bs.BeautifulSoup(source,'lxml')

    print(soup)

    driver = webdriver.Chrome()
    driver.get(url2)
    button = driver.find_element_by_id('//*[@id="main-content"]/div/div/div/div/ol[1]/li[2]/a')
    button.click()

if __name__ == '__main__':
    main()
