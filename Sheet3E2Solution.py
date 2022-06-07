#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maxschallwig
"""


import matplotlib.pyplot as plt
import datetime

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
        
        tempDate = [int(i) for i in processedLine[0].split("-")]

        tempDT = datetime.date(tempDate[0],tempDate[1],tempDate[2])
        
        price = float(processedLine[1])
        
        data["date"].append(tempDT)
        data["price"].append(price)

        
        
    return data
 
carrotData = readCSV("carrotPrices.csv")
onionData = readCSV("onionPrices.csv")

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)

ax.plot(carrotData["date"],carrotData["price"],c="orange",
        label="carrot")
ax.plot(onionData["date"],onionData["price"],c="purple",
        label="onion")

ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.set_title("Vegetable prices over 1 year timespan")

ax.legend(loc="lower left")


#1) To the plots created in Exercise 1 above, 
#add an annotation above the peak price for plot, 
#making the colour a light red
peakCarrotPrice = 0
peakCarrotCounter = 0
peakOnionCounter = 0

for i in range(len(carrotData["date"])):
    currentPrice = carrotData["price"][i]
    if currentPrice>peakCarrotPrice:
        peakCarrotPrice = currentPrice
        peakCarrotCounter = i
        
peakOnionCounter = onionData["price"].index(max(onionData["price"]))

ax.text(carrotData["date"][peakCarrotCounter],
        peakCarrotPrice+peakCarrotPrice*.02,
        str(round(peakCarrotPrice,2)),
        horizontalalignment = "center",
        verticalalignment = "center",
        color = (1,0,0,.6))

ax.text(onionData["date"][peakOnionCounter],
        onionData["price"][peakOnionCounter]+.01,
        str(round(onionData["price"][peakOnionCounter],2)),
        horizontalalignment = "center",
        verticalalignment = "center",
        color = (1,0,0,.6))


#2) Now also add the prices above the lowest price 
#for each plot, colouring them in light green

#3)Find a region on each of the graphs that shows 
#an increasing price and, for each plot, put the 
#price change per day in dark red next to this 
#increasing line

#4) Find a region on each of the graphs that 
#shows a decreasing price and, for each plot, 
#put the price change per day in dark green next 
#to this decreasing line

plt.show()