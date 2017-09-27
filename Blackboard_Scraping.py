import requests
from lxml import html
import bs4 as bs

USERNAME = "kazukis2"
PASSWORD = "u6MFDIFPgj"

LOGIN_URL = "https://compass2g.illinois.edu/webapps/login/?new_loc=%2Fwebapps%2Fblackboard%2Fcontent%2FlistContent.jsp%3Fcourse_id%3D_33306_1%26content_id%3D_2738572_1"
URL = "https://compass2g.illinois.edu/webapps/bb-mygrades-BBLEARN/myGrades?course_id=_33306_1&stream_name=mygrades&is_stream=false"
def main():
    session_requests = requests.session()

    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    #authenticity_token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]

    payload = {
        "user_id": USERNAME, 
        "password": PASSWORD, 
    }

    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    result = session_requests.get(URL, headers = dict(referer = URL))

    soup = bs.BeautifulSoup(result.text,'lxml')
    for url in soup.find_all('h3'):
        print(url)
    
if __name__ == '__main__':
    main()