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

#1) Create a figure of desired size and add a subplot to it.
fig = plt.figure(figsize=(8,8))
ax1 = fig.add_subplot(1,1,1)

#2) For your dataset create a new list for rounded values, 
#which contains the vegetable’s price for each date rounded 
#to the nearest cent (i.e. 0.01).

roundedCarrotPrice = []
for price in carrotData["price"]:
    roundedCarrotPrice.append(round(price,2))
    
roundedOnionPrice = []
for price in onionData["price"]:
    roundedOnionPrice.append(round(price,2))    
    

#3) Plot a histogram distribution of the range of prices 
#for your vegetable.
    
#4) Adjust the bins so that the lowest bin is 1 cent below 
#the minimum price and the highest bin is 1 cent above 
#the maximum price, with bin sizes being equal to one cent.
    

#5) Align the bins so that the center of the bin is directly 
#above the corresponding price
    
    
#6) Repeat step 2. & 3. from here for the other vegetable’s price, 
#and add its price histogram onto your already existing 
#histogram.
    
#7) Change the bin ranges to capture the price ranges of 
#both vegetables, and change the bin sizes to be 5 cents per bin.

#8) Change the color of each histogram to reflect the 
#color of the vegetable used in the previous exercise sheet.

#9) Add a title and labels to your graph and perform any 
#extra formatting you may want to.

minCarrotPrice = min(roundedCarrotPrice)
maxCarrotPrice = max(roundedCarrotPrice)
bins = []

absMinPrice = min(roundedCarrotPrice+roundedOnionPrice)
absMaxPrice = max(roundedCarrotPrice+roundedOnionPrice)

for i in range(int((absMinPrice-0.01)*100),int((absMaxPrice+0.01)*100)+1,5):
    bins.append(i/100)
ax1.hist((roundedCarrotPrice,roundedOnionPrice),bins=bins,
         align="left", color = ["orange","purple"])

ax1.set_xlabel("Price")
ax1.set_ylabel("Count")
ax1.set_title("Histogram distribution of carrot and onion prices")
plt.show()    





