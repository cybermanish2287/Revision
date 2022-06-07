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


#1) Choose one of the two vegetables and create a new list 
#where each element is the average price of that vegetable 
#for that month.

month = []
averageCarrotPrice = []
averageOnionPrice = []

previousMonth = 1
monthPricesCarrot = []
monthPricesOnion = []

for i in range(len(carrotData["date"])):
    currentMonth = carrotData["date"][i].month
    if currentMonth != previousMonth:
        avgMonthPriceCarrot = sum(monthPricesCarrot)/len(monthPricesCarrot)
        averageCarrotPrice.append(avgMonthPriceCarrot)
        
        avgMonthPriceOnion = sum(monthPricesOnion)/len(monthPricesOnion)
        averageOnionPrice.append(avgMonthPriceOnion)
        
        month.append(previousMonth)
        previousMonth = currentMonth
    else:
        monthPricesCarrot.append(carrotData["price"][i])
        monthPricesOnion.append(onionData["price"][i])
        
        
    if i == (len(carrotData["date"])-1):
        avgMonthPriceCarrot = sum(monthPricesCarrot)/len(monthPricesCarrot)
        averageCarrotPrice.append(avgMonthPriceCarrot)
        
        avgMonthPriceOnion = sum(monthPricesOnion)/len(monthPricesOnion)
        averageOnionPrice.append(avgMonthPriceOnion)
        
        month.append(previousMonth)


#2) Create a bar graph that plots each of the averaged prices 
#next to each other, in order of increasing month from left to right.

#3) Adjust the width of the bars to make them a bit thinner, 
#and change the alignment of them so that each bar is right 
#on top of the major axis tick.

#4) Now add on the other vegetable’s average price for each 
#month onto the same bar graph, stacking them so that each bar 
#ends at the average price for that vegetable for that month. 
#Make sure that both bar graphs have the same width.
        
#5) Adjust the color of each bar graph to represent the color 
#of each vegetable.
        
#6) Add an appropriate title, axes labels, axis tick names, 
#and a legend to the graph.

fig = plt.figure(figsize=(8,8))
ax1 = fig.add_subplot(1,1,1)

ax1.bar(month,
        averageOnionPrice,
        width = 0.35,
        align = "center",
        color = "purple",
        label = "onion")

ax1.bar(month,
        averageCarrotPrice,
        width = 0.35,
        align = "center",
        color = "orange",
        label = "carrot")


ax1.set_title("Average vegetable prices per month")
ax1.set_ylabel("Average Price")
ax1.set_xlabel("Month")

monthList = ["Jan.",
             "Feb.",
             "March",
             "April",
             "May",
             "June",
             "July",
             "Aug.",
             "Sept.",
             "Oct.",
             "Nov.",
             "Dec."]

plt.xticks(month,monthList)


plt.legend()

plt.show()



#1) For each month for each vegetable, find the minimum and 
#maximum price the vegetable took on that month, 
#and save each appropriately.

#2) For each vegetable’s bar graph in each month, 
#add in error bars that reflect the minimum and 
#maximum price of that vegetable for that month. 
#Color the error bars black.

#3) To reduce clutter, instead of plotting the bar graphs stacked, 
#adjust the graphs so that the bar graph for each vegetable is 
#plotted next to each other symmetrically around the major axis tick.



