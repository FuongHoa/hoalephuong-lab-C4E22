from youtube_dl import YoutubeDL
import pyexcel

# 1. Download a single youtube video:
# dl = YoutubeDL()
# dl.download(["https://www.youtube.com/watch?v=HXkh7EOqcQ4"])

# 2. Download multiple videos:
# dl = YoutubeDL()
# dl.download(["https://www.youtube.com/watch?v=Bmo4PSbB8E8", "https://www.youtube.com/watch?v=NLBTbCfR-Fg", "https://www.youtube.com/watch?v=dh2bpIuDz8U"])

# 3. Download audio:
# options = {
#     'format': 'bestaudio' # tell python download the highest quality
# }
# dl = YoutubeDL(options)
# dl.download(["https://www.youtube.com/watch?v=ji8cjaFUIU0"])

# 4. Search and download a video:
# options = {
#     'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
#     'max_downloads': 1 # Tell downloader to download only the first entry (video)
# }
# dl = YoutubeDL(options)
# dl.download(['paris in the rain Lauv'])

# 5. Search and download the first audio:
# options = {
#     'format': 'bestaudio',
#     'default_search': 'ytsearch',
#     'max_download': 1,
# }
# dl = YoutubeDL(options)
# dl.download(["https://www.youtube.com/watch?v=GTWqwSNQCcg"])