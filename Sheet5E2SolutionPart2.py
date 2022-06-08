#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maxschallwig
"""


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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
        
        country = processedLine[0]    
        price = float(processedLine[1])
        
        data["country"].append(country)
        data["price"].append(price)

        
        
    return data
 
countryCoords = {"Canada":{"x":150,
                           "bottom":80},
                "America":{"x":130,
                           "bottom":130},
                "Mexico":{"x":110,
                           "bottom":180},
                "China":{"x":650,
                           "bottom":150},
                "Australia":{"x":700,
                           "bottom":320},
    }
                
#1) Load and save the data points into a relevant format
carrotData = readCSV("carrotPrices_1.csv")
onionData = readCSV("onionPrices_1.csv")

minPrice = min(carrotData["price"])
maxPrice = max(carrotData["price"])
#print(carrotData)
img = mpimg.imread("worldMap.png")

spines = ["top","bottom","left","right"]
fig = plt.figure(figsize=(8,8))
ax1 = fig.add_subplot(111)

#5) To the right of the plot, add a color bar to help understand 
#what the colors mean in terms of prices.
#6) Add appropriate text to your graph
x = []
for i in range(100):
    x.append([i])
ax1.imshow(x,extent = [800,830,0,400],cmap="jet")

ax1.text(840,15,s=str(round(maxPrice,2)))
ax1.text(840,400,s=str(round(minPrice,2)))

ax1.imshow(img)


for spine in spines:
    ax1.spines[spine].set_visible(False)
    
ax1.yaxis.set_visible(False)
ax1.xaxis.set_visible(False)


#2) Plot each value as a bar on each country and 
#choose an appropriate bar height scale.

#3) Setup a colormap that corresponds to the range of values 
#covered by your prices
    
cm = plt.cm.get_cmap("jet",100)
colors = cm(range(100))

cC = 0

#4) Apply the colormap to your bars, changing the face color 
#of each bar to represent its price value.


for country in carrotData["country"]:
#for country,currentValue in zip(carrotData["country"],carrotData["price"]):
    currentValue = carrotData["price"][cC]
    height = -35 +(currentValue-minPrice)/(maxPrice-minPrice)*-35
    
    colorIndex = int(round((currentValue-minPrice)/
                           (maxPrice-minPrice)*100,0))-1
    if colorIndex < 0:
#        colorIndex = 0
        colorIndex += 1
    color = colors[colorIndex]
    
    ax1.bar(countryCoords[country]["x"],height,
            bottom=countryCoords[country]["bottom"],
            width = 10,
            color = color)
    
    cC += 1
    


ax1.set_title("Carrot price in different countries across the world")
plt.show()