import os
import requests
from bs4 import BeautifulSoup as BS
from raven import Client

DOCKER_NAME = os.environ.get("DOCKER_NAME","")
SENTRY_DNS = os.environ.get("SENTRY_DNS", "http://9b27dfdbe05447f295676178f192ba55:b6c43dfe896d4bb8b1ecdcb5da1e621b@45.79.73.83:9000/6")

session = requests.session()
headers = {
    "referer": "https://www.google.com.tw/",
    "user-agent": "mozilla/5.0 (x11; linux x86_64) applewebkit/537.36 "
                  "(khtml, like gecko) "
                  "chrome/46.0.2490.86 safari/537.36"}
session.headers.update(headers)
res = session.get('https://whatismyipaddress.com/')
soup = BS(res.text, "html5lib")
ip = [a.text for a in soup.select('#section_left a')][0]

client = Client(dsn = SENTRY_DNS, name = DOCKER_NAME)
client.captureMessage(ip)

def _get_session():
    session = requests.session()
    headers = {
        "referer": "https://www.amazon.com/",
        "user-agent": "mozilla/5.0 (x11; linux x86_64) applewebkit/537.36 "
                      "(khtml, like gecko) "
                      "chrome/46.0.2490.86 safari/537.36"}
    session.headers.update(headers)
    return session

def _get_product_url(product_id):
    return 'https://www.amazon.com/dp/' + product_id

pid = "B00XQ4Z1Q0"
url = _get_product_url(pid)
res = session.get(url)
soup = BS(res.text, "lxml")
print(soup.select("#dp-container")[0].text)
print("===================================")
print(soup.text)
