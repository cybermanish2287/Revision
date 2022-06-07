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

month = []
averageCarrotPrice = []
averageOnionPrice = []

previousMonth = 1
monthPricesCarrot = []
monthPricesOnion = []

#1) For each month for each vegetable, find the minimum and 
#maximum price the vegetable took on that month, 
#and save each appropriately.

minCarrotPrice = []
maxCarrotPrice = []
minOnionPrice = []
maxOnionPrice = []


for i in range(len(carrotData["date"])):
    currentMonth = carrotData["date"][i].month
    if currentMonth != previousMonth:
        avgMonthPriceCarrot = sum(monthPricesCarrot)/len(monthPricesCarrot)
        averageCarrotPrice.append(avgMonthPriceCarrot)
        
        avgMonthPriceOnion = sum(monthPricesOnion)/len(monthPricesOnion)
        averageOnionPrice.append(avgMonthPriceOnion)
        
        month.append(previousMonth)
        previousMonth = currentMonth
        
        minCarrotPrice.append(min(monthPricesCarrot))
        maxCarrotPrice.append(max(monthPricesCarrot))
        minOnionPrice.append(min(monthPricesOnion))
        maxOnionPrice.append(max(monthPricesOnion))
        
    else:
        monthPricesCarrot.append(carrotData["price"][i])
        monthPricesOnion.append(onionData["price"][i])
        
        
    if i == (len(carrotData["date"])-1):
        avgMonthPriceCarrot = sum(monthPricesCarrot)/len(monthPricesCarrot)
        averageCarrotPrice.append(avgMonthPriceCarrot)
        
        avgMonthPriceOnion = sum(monthPricesOnion)/len(monthPricesOnion)
        averageOnionPrice.append(avgMonthPriceOnion)
        
        month.append(previousMonth)
        
        minCarrotPrice.append(min(monthPricesCarrot))
        maxCarrotPrice.append(max(monthPricesCarrot))
        minOnionPrice.append(min(monthPricesOnion))
        maxOnionPrice.append(max(monthPricesOnion))

#2) For each vegetable’s bar graph in each month, 
#add in error bars that reflect the minimum and 
#maximum price of that vegetable for that month. 
#Color the error bars black.

for i in range(len(minCarrotPrice)):
    minCarrotPrice[i] = averageCarrotPrice[i] - minCarrotPrice[i]
    maxCarrotPrice[i] = maxCarrotPrice[i] - averageCarrotPrice[i]
    minOnionPrice[i] = averageOnionPrice[i] - minOnionPrice[i]
    maxOnionPrice[i] = maxOnionPrice[i] - averageOnionPrice[i]
    
    
#3) To reduce clutter, instead of plotting the bar graphs stacked, 
#adjust the graphs so that the bar graph for each vegetable is 
#plotted next to each other symmetrically around the major axis tick.


carrotError = [minCarrotPrice,maxCarrotPrice]    
onionError = [minOnionPrice,maxOnionPrice] 
carrotMonths = []
onionMonths = []

for m in month:
    carrotMonths.append(m-.35/2)
    onionMonths.append(m+.35/2)


fig = plt.figure(figsize=(8,8))
ax1 = fig.add_subplot(1,1,1)

ax1.bar(onionMonths,
        averageOnionPrice,
        width = 0.35,
        align = "center",
        color = "purple",
        label = "onion",
        yerr = onionError,
        ecolor = "black")

ax1.bar(carrotMonths,
        averageCarrotPrice,
        width = 0.35,
        align = "center",
        color = "orange",
        label = "carrot",
        yerr = carrotError,
        ecolor = "black")


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




