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
        for x in restData:
            finalData.append(int(x))
            
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

#        tempDate = processedLine[0].split("-")
#        for i in range(len(tempDate)):
#            tempDate[i] = int(tempDate[i])
#        print(tempDate)

        tempDT = datetime.date(tempDate[0],tempDate[1],tempDate[2])
        
        price = float(processedLine[1])
        
        data["date"].append(tempDT)
        data["price"].append(price)
#        print(data)
#        break
        
        
    return data
 
#txtVersionData = readTxt()
carrotData = readCSV("carrotPrices.csv")
print(carrotData)
#onionData = readCSV("onionPrices.csv")
