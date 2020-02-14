import requests

def fetch():
    data = requests.get('https://www.googleapis.com/youtube/v3/search?key=AIzaSyBCXt75NDt10P7isODOx12jBmIPxryBnjY&channelId=UCX6OQ3DkcsbYNE6H8uQQuVA&part=snippet,id&order=date&maxResults=20')
    data1 = data.json()
    data2 = data1['items']
    return data2
