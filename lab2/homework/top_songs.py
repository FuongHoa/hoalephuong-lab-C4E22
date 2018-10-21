from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
import pyexcel
url = "https://www.apple.com/itunes/charts/songs/"

conn = urlopen(url)
raw_data = conn.read()
webpage_text = raw_data.decode("utf-8")
options = {
    'default_search':'ytsearch',
    'max_download': 1,
    'format':'bestaudio/audio',
}

dl = YoutubeDL(options)

soup = BeautifulSoup(webpage_text, "html.parser")
section = soup.find('section','section chart-grid')
div = section.find("div", "section-content")
ul = div.find("ul")
li_list = ul.find_all("li")
songs_list = []
for li in li_list:
    a = li.h3.a
    song = a.string
    
    b = li.h4.a
    artist = b.string

# dl.download([song, artist])

    songs = {
        "Song": song,
        "Artist": artist,
    }
  
    songs_list.append(songs)

pyexcel.save_as(records=songs_list, dest_file_name="top_songs.xlsx")

