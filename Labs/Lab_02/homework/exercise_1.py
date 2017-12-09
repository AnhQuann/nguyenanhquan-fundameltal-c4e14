from youtube_dl import YoutubeDL
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

html_content = urlopen('https://www.apple.com/itunes/charts/songs/').read().decode('utf8')
soup = BeautifulSoup(html_content, 'html.parser')
section = soup.find('section', 'section chart-grid')
ul = section.find('ul')
li_list = ul.find_all('li')

songs_list = []

youtube_list = []

for li in li_list:
    h3 = li.h3
    h4 = li.h4
    a3 = h3.a
    a4 = h4.a
    songs = {
        'SONG': a3.string,
        'MUSICIAN': a4.string
    }
    youtube_list.append('{0} of {1}'.format(a3.string, a4.string))
    songs_list.append(songs)

# pyexcel.save_as(records = songs_list, dest_file_name = 'Top_100_iTunes.xlsx')

options = {
    'default_search': 'ytsearch', # just search, not download
    'max_downloads': len(youtube_list), # download only one audio
    'format': 'bestaudio/audio' # choose highest quality
}

dl = YoutubeDL(options)
for search_and_down in youtube_list:
    dl.download(search_and_down)
