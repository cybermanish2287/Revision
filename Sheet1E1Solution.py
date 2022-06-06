#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maxschallwig
"""

#Data Source - http://www.seanlahman.com/baseball-archive/statistics/ 
#Stats for 2017
import matplotlib.pyplot as plt

def readTxt():
    f = open("Sheet1E1.txt","r")
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
    f = open("Sheet1E1.csv","r")  
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


#1) Create a hits per at bat variable
print(data.keys())
HPAB = []

for i in range(len(data["Hits"])):
    if data["AtBase"][i] != 0:
        HPAB.append(data["Hits"][i]/data["AtBase"][i])
    else:
        HPAB.append(0)       
    

#2) Create a figure named HPABY, with size 8,8
        
fig = plt.figure("HPABY",figsize=(8,8))        

#3) Add an axis to the figure

ax = fig.add_subplot(1,1,1)

#4) Plot the HPAB against the number of games
#5) Make the size of the points appropriately small 
#so you can see a good separation between the data
#6) Have all points plotted in green 
ax.scatter(data["Games"],HPAB,s = 5,c = "green")

#7) Show the plot
plt.show()