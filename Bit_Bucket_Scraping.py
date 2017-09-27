import requests
from lxml import html

USERNAME = "shinkazuki99@gmail.com"
PASSWORD = "9vduWHWtfGj8"

LOGIN_URL = "https://bitbucket.org/account/signin/?next=/"
URL = "https://bitbucket.org/dashboard/repositories"

def main():
    session_requests = requests.session()

    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
        "csrfmiddlewaretoken": authenticity_token
    }

    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    print(bucket_names)

if __name__ == '__main__':
    main()
