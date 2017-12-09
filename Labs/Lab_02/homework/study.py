from youtube_dl import YoutubeDL

# 1. Download a single Youtube video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=3nQNiWdeH2Q'])

# 2. Download multiple youtube video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=3nQNiWdeH2Q', 'https://www.youtube.com/watch?v=-sYSj7KU-UI'])

# 3. Download audio
options = {
    'format': 'bestaudio/audio' # choose highest quality
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=JZjRrg2rpic'])

# 4. Search and then download the first video
options = {
    'default_search': 'ytsearch', # just search, not download
    'max_downloads': 1 # download download only one video
}
dl = YoutubeDL(options)
dl.download(['Time for a true display of skill'])

# Sample 5: Search and then download the first audio
options = {
    'default_search': 'ytsearch', # just search, not download
    'max_downloads': 1, # download only one audio
    'format': 'bestaudio/audio' # choose highest quality
}
dl = YoutubeDL(options)
dl.download(['Time for a true display of skill'])
