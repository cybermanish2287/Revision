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
 
#1) Read and understand the two attached data files 
#in whichever format you prefer 
#2) Load in each data set and save it in 
#appropriately named variables
    
#carrotData = readTxt("carrotPrices.txt")
carrotData = readCSV("carrotPrices.csv")
onionData = readCSV("onionPrices.csv")


#3) Create a new figure, size 8,8, 
#with one subplot, and plot both the onion 
#as well as the carrot prices on the same graph

#4) Make the colour of the onion plot purple
#5) Make the colour of the carrot plot orange
#6) Add a label you deem appropriate to each plot 

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)

ax.plot(carrotData["date"],carrotData["price"],c="orange",
        label="carrot")
ax.plot(onionData["date"],onionData["price"],c="purple",
        label="onion")

#7) Label the axes as well as add a title to your graph 
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.set_title("Vegetable prices over 1 year timespan")

#8) Add a legend to the graph and then show the graph

ax.legend(loc="lower left")
plt.show()