from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel 
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")

f = open("optional.html", "wb")
f.write(raw_data)
f.close()

soup = BeautifulSoup(webpage_text, "html.parser")

table = soup.find('table',{'style':'border-top: solid 1px #e6e6e6;border-left:solid 1px #cccccc;border-bottom:solid 1px #cccccc'})
tr_list = table.find_all('tr')
report =[]

for tr in tr_list:
    td_list = tr.find_all("td")
    for td in td_list:
        td = {
            "Content": td_list[0].string,
            "Quy 4-2016": td_list[1].string,
            "Quy 1-2017": td_list[2].string,
            "Quy 2-2017": td_list[3].string,
            "Quy 3-2017": td_list[4].string,
        }
    report.append(td)
pyexcel.save_as(records = report, dest_file_name = "optional.xlsx")
