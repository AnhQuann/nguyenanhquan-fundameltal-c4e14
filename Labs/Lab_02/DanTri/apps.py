from urllib.request import urlopen 
from bs4 import BeautifulSoup # Camel Case
import pyexcel

# 1. Download dantri homepage
webpage = urlopen('http://dantri.com.vn') # Open connection
data = webpage.read()
html_content = data.decode('utf8')

# 2. Analyze ROI(Region Of Interest)
# 2.1 Create BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
ul = soup.find('ul', 'ul1 ulnew') # find one
li_list = ul.find_all('li')
# print(li_list[0].prettify())
news_list = []

for li in li_list:
    h4 = li.h4 # find(h4)
    a = h4.a
    # print(a.string) # lay ten cua link
    news = {
        'title': a.string,
        'link': a['href']
    }
    news_list.append(news)
# print(news_list)

pyexcel.save_as(records=news_list, dest_file_name="dantri.xlsx")

# 3. Extract data from ROI
