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
    request = requests.get('http://api.musixmatch.com/ws/1.1/track.search?q_artist='+artist+'&apikey='+api_key)
    if request.status_code == 200:
        trackList = request.json()['message']['body']['track_list']
        for j in trackList:
            trackName=j['track']['track_name']
            print(trackName)
            if trackName not in songsDone:
                print(trackName)
                songsDone.append(trackName)
                url = 'https://api.lyrics.ovh/v1/'+artist+'/'+trackName
                request1 = requests.get(url)
                if request1.status_code == 200:
                    response_body = request1.text.lower()
                    match = re.findall(phrase.lower(), response_body)
                    print(match)
                    sum1 += (len(match))
        return sum1
    else:
        return(-1)

def visualize():
    x = np.array([ 0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20., 21., 22., 23., 24., 25., 26., 27., 28., 29.]) 
    y = np.array([ 0., 25., 27., 4., -22., -28., -8., 19., 29., 12., -16., -29., -16., 12., 29., 19., -8., -28., -22., 4., 27., 25., -0., -25., -27., -3., 22., 28., 8., -19.])
    plt.subplot(2,1,1)
    plt.plot(x,y)
    plt.title('LineGraph')
    plt.subplot(2,2,3)
    plt.hist((x,y))
    plt.title('Histogram')
    plt.subplot(2,2,4)
    plt.scatter(x,y)
    plt.title('Scatter')
    return plt.show()