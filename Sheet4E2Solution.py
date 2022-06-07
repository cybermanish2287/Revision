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
ax1 = fig.add_subplot(1,1,1)

roundedCarrotPrice = []
for price in carrotData["price"]:
    roundedCarrotPrice.append(round(price,2))
    
roundedOnionPrice = []
for price in onionData["price"]:
    roundedOnionPrice.append(round(price,2))    

minCarrotPrice = min(roundedCarrotPrice)
maxCarrotPrice = max(roundedCarrotPrice)
bins = []

absMinPrice = min(roundedCarrotPrice+roundedOnionPrice)
absMaxPrice = max(roundedCarrotPrice+roundedOnionPrice)

#1) To the histograms created in Exercise 1, add a legend 
#for each histogram.

for i in range(int((absMinPrice-0.01)*100),int((absMaxPrice+0.01)*100)+1,5):
    bins.append(i/100)
N,bins,patches = ax1.hist((roundedCarrotPrice,roundedOnionPrice),bins=bins,
         align="left", color = ["orange","purple"])



#meanCarrot = sum(roundedCarrotPrice)/len(roundedCarrotPrice)
#meanOnion = sum(roundedOnionPrice)/len(roundedOnionPrice)

meanCarrot = sum(carrotData["price"])/len(carrotData["price"])
meanOnion = sum(onionData["price"])/len(onionData["price"])

meanCarrotIndex = 0
meanOnionIndex = 0

for i in range(len(bins)-1):
    lowerBound = bins[i]
    upperBound = bins[i+1]
    if meanCarrot>= lowerBound:
        if meanCarrot<upperBound:
            meanCarrotIndex = i
            
    if meanOnion>= lowerBound:
        if meanOnion<upperBound:
            meanOnionIndex = i

#2) For each histogram, change the color of the bar that 
#contains the mean value to blue/green for the carrot/onion 
#dataset respectively.
           
            
#3) Add to the legend a label for each of the mean 
#values shown above, so that these values can easily 
#be understood.
            
patches[0][meanCarrotIndex].set_facecolor("blue")
patches[1][meanOnionIndex].set_facecolor("green")

labels = ["Carrot","Onion","Mean Carrot Price","Mean Onion Price"]
plt.legend([patches[0][0],patches[1][-1],patches[0][meanCarrotIndex],patches[1][meanOnionIndex]],labels)

ax1.set_xlabel("Price")
ax1.set_ylabel("Count")
ax1.set_title("Histogram distribution of carrot and onion prices")
plt.show()   

#print(bins) 




