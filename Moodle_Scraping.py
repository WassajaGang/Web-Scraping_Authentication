import requests
from lxml import html
import bs4 as bs
import urllib.request

USERNAME = "kazukis2"
PASSWORD = "u6MFDIFPgj"

LOGIN_URL = "https://www.lon-capa.illinois.edu/"
URL = "https://learn.illinois.edu/grade/report/user/index.php?id=23714"
def main():
    session_requests = requests.session()

    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    #authenticity_token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]

    payload = {
        "j_username": USERNAME, 
        "j_password": PASSWORD
    }

    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    result = session_requests.get(URL, headers = dict(referer = URL))
    
    sauce = urllib.request.urlopen(URL).read()
    soup = bs.BeautifulSoup(sauce,'lxml')
    
    for url in soup.find_all('h3'):
        print(url)
    

if __name__ == '__main__':
    main()
