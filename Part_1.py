import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce,'lxml')

#print(soup.findAll('p'))

'''
for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))
'''
'''
for url in soup.find_all('a'):
    print(url.get('href'))
'''
print(soup.get_text())