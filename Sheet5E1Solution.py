#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maxschallwig
"""


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def readTxt(fileName):
    f = open(fileName,"r")
    data = {}
    
    for line in f:
        part1 = line.strip("\n").split(" ")
        dataName = part1[0]
        restData = part1[1:]
        
        finalData = []
        if dataName == "date":
            for dateString in restData:
                tempDate = [int(i) for i in dateString.split("-")]
                finalData.append(datetime.date(tempDate[0],tempDate[1],tempDate[2]))
        elif dataName == "price":
            finalData = [float(i) for i in restData]
        data[dataName] = finalData
        
    f.close()
    return data

def readCSV(fileName):
    f = open(fileName,"r")  
    data = {}
    
    firstLine = f.readline().strip("\n").split(",")[1:]

    for name in firstLine:
        data[name] = []    
    
    for line in f:
        processedLine = line.strip("\n").split(",")[1:]
        
        country = processedLine[0]    
        price = float(processedLine[1])
        
        data["country"].append(country)
        data["price"].append(price)

        
        
    return data
 
carrotData = readCSV("carrotPrices_1.csv")
onionData = readCSV("onionPrices_1.csv")

#1) Import the image of the world map
img = mpimg.imread("worldMap.png")

#2) Display the image of the world map
#3) Remove the spines and axis ticks to make the image appear 
#as just the map
spines = ["top","bottom","left","right"]
fig = plt.figure(figsize=(8,8))
ax1 = fig.add_subplot(111)

ax1.imshow(img)

for spine in spines:
    ax1.spines[spine].set_visible(False)
    
ax1.yaxis.set_visible(False)
ax1.xaxis.set_visible(False)
plt.show()