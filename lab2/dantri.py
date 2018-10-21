# 1. Download the webpage
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel 
url = "https://dantri.com.vn"

# 1.1 Open a connection
conn = urlopen(url)

# 1.2 Download raw data
raw_data = conn.read()

# 1.3 Decode data
webpage_text = raw_data.decode("utf-8")

#1.4 Save text
# w - write
# b - binary
# f = open("dantri.html", "wb")
# f.write(raw_data)
# f.close()

# 2. Extract ROI
# 2.1 Convert text to soup
soup = BeautifulSoup(webpage_text, "html.parser")
# print(soup.prettify())
ul = soup.find("ul", "ul1 ulnew") 
# soup.find("div", id ="")
# print(ul.prettify())
li_list = ul.find_all("li")
# li = li_list[0]
news_list = []
# print(li.prettify())
for li in li_list:
    a = li.h4.a
    title = a.string
    link = url + a["href"]

    # print(title)
    # print(link)

    news = {
        "Title": title,
        "Link": link,
    }
    news_list.append(news)

# print(*news_list, sep="\n")
# print(li_list)
# for li in li_list:
    # print(li.prettify())
    # print("***********")

# 3. Extract Data



# 4. Save Data
pyexcel.save_as(records=news_list, dest_file_name="dantri.xls")