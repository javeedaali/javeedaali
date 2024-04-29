import requests
from bs4 import BeautifulSoup

url = "https://pixelford.com/blog/"
response = requests.get(url, headers = {'user-agent':'SlimShady'})

soup = BeautifulSoup(response.content, 'html.parser')

a_tags = soup.find_all("a", class_ = "entry-title-link")
for a_tag in a_tags:
    print(a_tag.get_text())
