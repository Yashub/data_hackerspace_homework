import requests
import re
import matplotlib.pyplot as plt
import numpy as np
from apikey import *


def lyrics_word_count_easy(artist, song, phrase):
    url = 'https://api.lyrics.ovh/v1/'+artist+'/'+song
    request = requests.get(url)
    if request.status_code == 200:
        response_body = request.text.lower()
        match = re.findall(phrase.lower(), response_body)
        return(len(match))
    else:
        return (-1)

def lyrics_word_count(artist, phrase):
    songsDone = []
    sum1 = 0
    api_key = apikey['api_key']
    request = requests.get('http://api.musixmatch.com/ws/1.1/artist.search?q_artist='+artist+'&apikey='+api_key)
    if request.status_code == 200:
        artistJSON = request.json()['message']['body']['artist_list'][0]['artist']
        artistName = artistJSON['artist_name']
        if artistName.lower()!=artist.lower():
            return(-1)
        artistID = str(artistJSON['artist_id'])
        albumList = requests.get('http://api.musixmatch.com/ws/1.1/artist.albums.get?artist_id='+artistID+'&g_album_name=1&apikey='+api_key).json()['message']['body']['album_list']
        for i in albumList:
            albumID=str(i['album']['album_id'])
            trackList = requests.get('http://api.musixmatch.com/ws/1.1/album.tracks.get?album_id='+albumID+'&apikey='+api_key).json()['message']['body']['track_list']
            for j in trackList:
                trackName=j['track']['track_name']
                if trackName not in songsDone:
                    songsDone.append(trackName)
                    url = 'https://api.lyrics.ovh/v1/'+artist+'/'+trackName
                    request1 = requests.get(url)
                    if request1.status_code == 200:
                        response_body = request1.text.lower()
                        match = re.findall(phrase.lower(), response_body)
                        sum1 += (len(match))
        return sum1
    else:
        return(-1)

def visualize():
    x = np.array([ 0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20., 21., 22., 23., 24., 25., 26., 27., 28., 29.]) 
    y = np.array([ 0., 25., 27., 4., -22., -28., -8., 19., 29., 12., -16., -29., -16., 12., 29., 19., -8., -28., -22., 4., 27., 25., -0., -25., -27., -3., 22., 28., 8., -19.])
    plt.plot(x,y)
visualize()