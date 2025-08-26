# inspecting web page in HTML
# BeautifulSoup and request

# from bs4 import BeautifulSoup
# import requests
# url = "https://www.scrapethissite.com/pages/forms/"
# page = requests.get(url)
# soup = BeautifulSoup(page.text, "html")
# print(soup)

# divcode = soup.find_all("p",class_ = "lead")
# print(divcode)

# print(soup.find("p" , class_ = "lead").text.strip())

# print(soup.find_all("th"))



# Scraping Data from a real website + pandas
from bs4 import BeautifulSoup
import requests
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url)
soup = BeautifulSoup(page.text , "html")
print(soup)