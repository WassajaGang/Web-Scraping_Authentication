import requests
from lxml import html
import bs4 as bs

USERNAME = "shinkazuki99@gmail.com"
PASSWORD = "5xUsVUEUhJiZ"

LOGIN_URL = "https://github.com/login"
URL = "https://github.com/shinkazuki99"

def main():
    session_requests = requests.session()

    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]

    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
        "csrfmiddlewaretoken": authenticity_token
    }

    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    result = session_requests.get(URL, headers = dict(referer = URL))
    soup = bs.BeautifulSoup(result.text,'lxml')
    
    for url in soup.find_all('span'):
        title = url.get('title')
        if title is not None:
            print(title)
    
if __name__ == '__main__':
    main()
