# Bai nay em chua lam xong
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

html_content = urlopen('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn').read().decode('utf8')
soup = BeautifulSoup(html_content, 'html.parser')

table_content = soup.find('table', id = 'tableContent')
tr_list = table_content.find_all('tr')
bold_text_list = [0, 1, 2, 4, 11, 14, 15, 18, 20]
normal_text_list = [3, 5, 6, 7, 8, 9, 10, 12, 13, 16, 17, 19, 21, 22, 23]

for tr in range(len(tr_list)):
    if tr in bold_text_list:
        td_list_string_bold = tr_list[tr].find_all('td', style = "width:32%;color:#014377;font-weight:bold;")
        td_list_number_bold = tr_list[tr].find_all('td', style = "width:15%;padding:4px;color:#014377;font-weight:bold;")
    elif tr in normal_text_list:
        td_list_string_normal = tr_list[tr].find_all('td', style = "width:32%;color:#014377;")
        td_list_number_normal = tr_list[tr].find_all('td', style = "width:15%;padding:4px;color:#014377;")

print(td_list_string_normal)
