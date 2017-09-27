import requests
from lxml import html
import bs4 as bs

USERNAME = "kazukishin_"
PASSWORD = "p9H7Wpe0e62#G&Hv"

LOGIN_URL = "https://www.instagram.com/accounts/login/?hl=en"
URL = "https://www.instagram.com/?hl=en"

def main():
    session_requests = requests.session()

    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
 
    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
        "csrf_token": 'cdDRSsaSWMzaHznM4xtEvghGO6vs2JLE'
    }

    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    result = session_requests.get(URL, headers = dict(referer = URL))
    soup = bs.BeautifulSoup(result.text,'lxml')
    
    for paragraph in soup.find_all('script'):
        print(paragraph.string)
        print(str(paragraph.text))

if __name__ == '__main__':
    main()
