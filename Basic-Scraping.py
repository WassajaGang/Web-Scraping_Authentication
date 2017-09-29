import requests
from lxml import html
import bs4 as bs
import urllib.request

def main():
    url = "http://www.bloomberg.com/quote/SPX:IND"
    url2 = "https://pythonprogramming.net/parsememcparseface/"
    url3 = "http://www.unc.edu/~mnbr/comp101/extra2/"
    url4 = "https://learn.illinois.edu/"
    
    source = urllib.request.urlopen(url4).read()
    soup = bs.BeautifulSoup(source,'lxml')

    table = soup.table
    table = soup.find('table')
    table_rows = table.find_all('tr')

    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        print(row)

if __name__ == '__main__':
    main()
