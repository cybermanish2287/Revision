#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maxschallwig
"""

#Data Source - http://www.seanlahman.com/baseball-archive/statistics/ 
#Stats for 2017

import matplotlib.pyplot as plt

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
print(data.keys())

#1) Create a hits per at bat variable
HPAB = []
for i in range(len(data["Hits"])):
    if data["AtBase"][i]!= 0:
        HPAB.append(data["Hits"][i]/data["AtBase"][i])
    else:
        HPAB.append(0)

#2) Create a figure named HPABY, with size 10,10 
fig = plt.figure("HPABY",figsize=(10,20)) #w,h

#3) Add an axis to the figure
ax = fig.add_subplot(2,1,1)

#4) Plot the HPAB against the year it occurred at
#5) Have the line shown in green
ax.plot(data["Year"],HPAB,c="g")

#6) Show the plot
#plt.show()

#Create a second line plot that plots the at bat 
#versus the year they occurred at.

#1) Using the above figure, add an a second axis to the 
#figure, and re-format the first subplot so that they 
#stack on top of each other in two rows.
ax2 = fig.add_subplot(2,1,2)

#2) Plot the AB against the year it occurred at
#3) Have the line shown in purple
ax2.plot(data["Year"],data["AtBase"],c="purple")

#4) Show the plot
plt.show()



#Now we’re going to adjust the figure to make both of the axes 
#about square looking. 

#1. Adjust the figure height or width so that both axes look 
#about square