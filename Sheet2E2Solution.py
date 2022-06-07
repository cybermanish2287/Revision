#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maxschallwig
"""

#Data Source - http://www.seanlahman.com/baseball-archive/statistics/ 
#Stats for 2017

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def readTxt():
    f = open("Sheet1E2.txt","r")
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

def readCSV():
    f = open("Sheet1E2.csv","r")  
    data = {}
    
    firstLine = f.readline().strip("\n").split(",")[1:]

    for name in firstLine:
        data[name] = []    
    
    for line in f:
        processedLine = line.strip("\n").split(",")[1:]
        
        for index in range(len(processedLine)):
            name = firstLine[index]
            dataPoint = int(processedLine[index])
            data[name].append(dataPoint)
        
    return data
 
#txtVersionData = readTxt()
data = readCSV()

HPAB = []
for i in range(len(data["Hits"])):
    if data["AtBase"][i]!= 0:
        HPAB.append(data["Hits"][i]/data["AtBase"][i])
    else:
        HPAB.append(0)


majorLocator = MultipleLocator(10)
minorLocator = MultipleLocator(2)

fig = plt.figure("HPABY",figsize=(10,20)) #w,h
ax = fig.add_subplot(2,1,1)
ax.plot(data["Year"],HPAB,c="g")
ax2 = fig.add_subplot(2,1,2)
ax2.plot(data["Year"],data["AtBase"],c="purple")

ax.set_ylim(0,1)
ax.set_xlim(data["Year"][0]-1,data["Year"][-1]+1)


ax2.set_ylim(0,550)
ax2.set_xlim(data["Year"][0]-1,data["Year"][-1]+1)

ax.set_xlabel("Year")
ax.set_ylabel("HPAB")
ax.set_title("HPAB for each Year")

ax2.set_xlabel("Year")
ax2.set_ylabel("At Base Count")
ax2.set_title("At Base Count for each Year")


ax.xaxis.set_major_locator(majorLocator)
ax.xaxis.set_minor_locator(minorLocator)

ax2.xaxis.set_major_locator(majorLocator)
ax2.xaxis.set_minor_locator(minorLocator)

#1) Create a list containing the names for each 
#of the major ticks that will be replaced 
#e.g. 80’s, 90’s, 00’s, ...

majorLabels = []

for tempValue in ax.get_xticks().tolist():
    intValue = int(tempValue)
    strValue = str(intValue)
    formatedValue = strValue[-2:]+"'s"
    majorLabels.append(formatedValue)
    
#2) Create a list containing the names for each
# of the minor ticks that will be replaced
# e.g. ’82, ’84, ’86, ...

minorLabels = []
for tempValue in range(1882,1921,2):
    if tempValue%10 == 0:
        minorLabels.append("")
    else:
        strValue = str(tempValue)
        formatedValue = "'"+strValue[-2:]
        minorLabels.append(formatedValue)
        
#3) Specify and change out the appropriate
# major and minor ticks

ax.set_xticklabels(majorLabels)
ax2.set_xticklabels(majorLabels)

ax.set_xticklabels(minorLabels,minor=True)
ax2.set_xticklabels(minorLabels,minor=True)

plt.show()