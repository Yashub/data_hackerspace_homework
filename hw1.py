#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np

def histogram_times(filename):
    fh = open(filename, 'r')
    hours = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    reader = csv.reader(fh)
    fh.close()
    for line in reader:
        hour = line[1].split(":")[0]
        if hour.isdigit():
            hours[int(hour)%24]=hours[int(hour)%24]+1
        else:
            continue
def weigh_pokemons(filename, weight):
    fh = open(filename, 'r')
    j = json.load(fh)
    fh.close()
    output = []
    weight = str(weight) + " kg"
    for i in j["pokemon"]:
        if i["weight"]==weight:
            output.append(i["name"])
    return output
                          
def single_type_candy_count(filename):
    fh = open(filename, 'r')
    j = json.load(fh)
    fh.close()
    sum = 0
    for i in j["pokemon"]:
        if len(i["type"])==1:
            try:
                sum += i["candy_count"]
            except:
                continue
    return sum

def reflections_and_projections(points):
    y = points[1]
    x = points[0]
    y = 2-y
    temp = x
    x = -y
    y = temp
    temp = 0.1*(3*x+9*y)
    x = 0.1*(x+3*y)
    y = temp
    a = np.array([x,y])
    return a

def normalize(image):
    max1 = 0
    min1 = 255
    for i in image:
        for j in i:
            if j>max1:
                max1 = j
            if j<min1:
                min1 = j
    print(max1,min1)
    if min1==max1:
        return image
    a = (255/(max1-min1))*(image-min1)
    return a

def sigmoid_normalize(image, a):
    b = (255)*((1+np.exp(((-a)^(-1))*(image-128)))^-1)
    return b


