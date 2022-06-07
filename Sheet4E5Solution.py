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


#1) For each vegetable, create a box and whisker plot and show them 
#next to each other on the same graph.

#2) Change the whiskers so that the ends of the whiskers go to the 
#10th and 90th percentile of each vegetable’s price.

#3) Add a notch to the box and whisker plot for each vegetable.

#4) Adjust the confidence interval of each vegetable’s box 
#and whisker plot to be 5 cents in either direction around 
#the median value.



#[1,2,3] -> med = 2 len(3)/2 -> 1.5 - > index = 1
#[1,2,3,4] -> 2.5 (2+3)/2

#[3,1,2] -> [1,2,3] -> median

medianIndex = int(len(carrotData["price"])/2)

#carrotData["price"].sort()
#onionData["price"].sort()

carrotPriceCopy = carrotData["price"].copy()
onionPriceCopy = onionData["price"].copy()

carrotPriceCopy.sort()
onionPriceCopy.sort()


medO = onionPriceCopy[medianIndex]
medC = carrotPriceCopy[medianIndex]


fig = plt.figure(figsize=(8,8))

ax1 = fig.add_subplot(1,1,1)

ax1.boxplot(x = [carrotData["price"],onionData["price"]],
            whis = [10,90],
            notch = True,
            conf_intervals = [[medC-0.05,medC+0.05],[medO-0.05,medO+0.05]])


ax1.set_title("Price distribution for onions and carrots")
ax1.set_ylabel("Price")
ax1.set_xlabel("Vegetable")
plt.xticks([1,2],["Carrot","Onion"])
plt.show()
