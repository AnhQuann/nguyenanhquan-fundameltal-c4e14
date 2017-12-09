from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

html_content = urlopen('https://www.nhaccuatui.com/').read().decode('utf8')
soup = BeautifulSoup(html_content, 'html.parser')
div = soup.find('div', 'list_chart_music', id = 'top20-content')
ul = div.find('ul')
li_list = ul.find_all('li')

songs_list =[]

for li in li_list:
    h3 = li.h3
    a3 = h3.a
    h4 = li.h4
    a_list = h4.find_all('a')
    musician_list = []
    for a in a_list:
        musician_list.append(a.string)
        # a_string = a.string
    songs = {
        'SONG': a3.string,
        'MUSICIAN':', '.join(musician_list)
    }
    songs_list.append(songs)


# print(songs_list)
pyexcel.save_as(records = songs_list, dest_file_name="nhaccuatuii.xlsx")

# Kiem tra xem co scraft dc ko

# file = open('nct.html', 'wb') # write binary(raw)
# file.write(raw_data)
# file.close()
