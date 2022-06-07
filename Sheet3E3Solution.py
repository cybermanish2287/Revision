#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maxschallwig
"""


import matplotlib.pyplot as plt
import datetime

#print(plt.style.available)

#plt.style.use("ggplot")

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

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)

ax.plot(carrotData["date"],carrotData["price"],c="orange",
        label="carrot")
ax.plot(onionData["date"],onionData["price"],c="purple",
        label="onion")

ax.set_xlabel("Date",fontsize=12)
ax.set_ylabel("Price",fontsize=12)
ax.set_title("Vegetable prices over 1 year timespan",
             fontsize = 15)

ax.legend(loc="lower left")

peakCarrotPrice = 0
peakCarrotCounter = 0
peakOnionCounter = 0

for i in range(len(carrotData["date"])):
    currentPrice = carrotData["price"][i]
    if currentPrice>peakCarrotPrice:
        peakCarrotPrice = currentPrice
        peakCarrotCounter = i
        
peakOnionCounter = onionData["price"].index(max(onionData["price"]))

ax.text(carrotData["date"][peakCarrotCounter],
        peakCarrotPrice+peakCarrotPrice*.02,
        str(round(peakCarrotPrice,2)),
        horizontalalignment = "center",
        verticalalignment = "center",
        color = (1,0,0,.6))

ax.text(onionData["date"][peakOnionCounter],
        onionData["price"][peakOnionCounter]+.01,
        str(round(onionData["price"][peakOnionCounter],2)),
        horizontalalignment = "center",
        verticalalignment = "center",
        color = (1,0,0,.6))


minOnionCounter = onionData["price"].index(min(onionData["price"]))
minCarrotCounter = carrotData["price"].index(min(carrotData["price"]))

ax.text(carrotData["date"][minCarrotCounter],
        carrotData["price"][minCarrotCounter]-0.01,
        str(round(carrotData["price"][minCarrotCounter],2)),
        horizontalalignment = "center",
        verticalalignment = "center",
        color = "green")


ax.text(onionData["date"][minOnionCounter],
        onionData["price"][minOnionCounter]-0.01,
        str(round(onionData["price"][minOnionCounter],2)),
        horizontalalignment = "center",
        verticalalignment = "center",
        color = "green")

maxRange = 0
bucketNumber = 0

minRange = 0
minBucketNumber = 0

bucketCounter = 0
for i in range(0,365,50):
    bucket = onionData["price"][i:i+50]
    minBucketVal = min(bucket)
    maxBucketVal = max(bucket)
    minBucketIndex = bucket.index(min(bucket))
    maxBucketIndex = bucket.index(max(bucket))
    bucketRange = maxBucketVal-minBucketVal
    minBucketRange = minBucketVal-maxBucketVal
    
    if minBucketIndex < maxBucketIndex:
        if bucketRange > maxRange:
            maxRange = bucketRange
            bucketNumber = bucketCounter
            
    elif maxBucketIndex < minBucketIndex:
        if minBucketRange < minRange:
            minRange = minBucketRange
            minBucketNumber = bucketCounter
        
    bucketCounter += 1

minBucket = onionData["price"][50*minBucketNumber:50*minBucketNumber+50]
minDateBucket = onionData["date"][50*minBucketNumber:50*minBucketNumber+50]
minLowerBucketIndex = minBucket.index(min(minBucket))
minUpperBucketIndex = minBucket.index(max(minBucket))

minTimeDifference = (minDateBucket[minLowerBucketIndex]-minDateBucket[minUpperBucketIndex])
minTimeDifference = minTimeDifference.days

minPriceChange = min(minBucket)-max(minBucket)

minPriceChangePerDay = minPriceChange/minTimeDifference
   
minIncrementIndex = 50*minBucketNumber+int((minLowerBucketIndex-minUpperBucketIndex)/2)+minUpperBucketIndex

minXLocation = onionData["date"][minIncrementIndex]
minYLocation = onionData["price"][minIncrementIndex]
    
ax.text(minXLocation,
        minYLocation+0.05,
        str(round(minPriceChangePerDay,3)),
        horizontalalignment = "center",
        verticalalignment = "center",
        color = "darkgreen",
        weight = "bold")

bucket = onionData["price"][50*bucketNumber:50*bucketNumber+50]
dateBucket = onionData["date"][50*bucketNumber:50*bucketNumber+50]
minBucketIndex = bucket.index(min(bucket))
maxBucketIndex = bucket.index(max(bucket))

timeDifference = (dateBucket[maxBucketIndex]-dateBucket[minBucketIndex])
timeDifference = timeDifference.days

priceChange = max(bucket)-min(bucket)

priceChangePerDay = priceChange/timeDifference


incrementIndex = 50*bucketNumber+int((maxBucketIndex-minBucketIndex)/2)+minBucketIndex

xLocation = onionData["date"][incrementIndex]
yLocation = onionData["price"][incrementIndex]

ax.text(xLocation,
        yLocation+0.05,
        str(round(priceChangePerDay,3)),
        horizontalalignment = "right",
        verticalalignment = "center",
        color = "darkred",
        weight = "bold")

#Carrot 
maxRange = 0
bucketNumber = 0

minRange = 0
minBucketNumber = 0

bucketCounter = 0
for i in range(0,365,50):
    bucket = carrotData["price"][i:i+50]
    minBucketVal = min(bucket)
    maxBucketVal = max(bucket)
    bucketRange = maxBucketVal-minBucketVal
    minBucketIndex = bucket.index(min(bucket))
    maxBucketIndex = bucket.index(max(bucket))
    minBucketRange = minBucketVal-maxBucketVal
    
    if minBucketIndex < maxBucketIndex:
        if bucketRange > maxRange:
            maxRange = bucketRange
            bucketNumber = bucketCounter
            
    elif maxBucketIndex < minBucketIndex:
        if minBucketRange < minRange:
            minRange = minBucketRange
            minBucketNumber = bucketCounter
        
    bucketCounter += 1
    
    
minBucket = carrotData["price"][50*minBucketNumber:50*minBucketNumber+50]
minDateBucket = carrotData["date"][50*minBucketNumber:50*minBucketNumber+50]
minLowerBucketIndex = minBucket.index(min(minBucket))
minUpperBucketIndex = minBucket.index(max(minBucket))

minTimeDifference = (minDateBucket[minLowerBucketIndex]-minDateBucket[minUpperBucketIndex])
minTimeDifference = minTimeDifference.days

minPriceChange = min(minBucket)-max(minBucket)

minPriceChangePerDay = minPriceChange/minTimeDifference
   
minIncrementIndex = 50*minBucketNumber+int((minLowerBucketIndex-minUpperBucketIndex)/2)+minUpperBucketIndex

minXLocation = carrotData["date"][minIncrementIndex]
minYLocation = carrotData["price"][minIncrementIndex]
    
ax.text(minXLocation,
        minYLocation+0.04,
        str(round(minPriceChangePerDay,3)),
        horizontalalignment = "left",
        verticalalignment = "center",
        color = "darkgreen",
        weight = "bold")

bucket = carrotData["price"][50*bucketNumber:50*bucketNumber+50]
dateBucket = carrotData["date"][50*bucketNumber:50*bucketNumber+50]
minBucketIndex = bucket.index(min(bucket))
maxBucketIndex = bucket.index(max(bucket))

timeDifference = (dateBucket[maxBucketIndex]-dateBucket[minBucketIndex])
timeDifference = timeDifference.days

priceChange = max(bucket)-min(bucket)

priceChangePerDay = priceChange/timeDifference


incrementIndex = 50*bucketNumber+int((maxBucketIndex-minBucketIndex)/2)+minBucketIndex

xLocation = carrotData["date"][incrementIndex]
yLocation = carrotData["price"][incrementIndex]

ax.text(xLocation,
        yLocation+0.08,
        str(round(priceChangePerDay,3)),
        horizontalalignment = "center",
        verticalalignment = "center",
        color = "darkred",
        weight = "bold")


ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

ax.yaxis.set_ticks_position("left")
ax.xaxis.set_ticks_position("bottom")


plt.savefig("OneYearVegetablePrices.png")

plt.show()


#1) To start off, adjust the font sizes of all of your labels, 
#annotations, and titles to make them big enough that they’re 
#legible, without making them too large though that they look 
#clunky

#2) Choose the elements that you think are most important 
#and make their text bold to help them stand out from the rest

#3) Remove the right and top spine of your axis, so that 
#your data doesn’t look boxed in


#4) Pick one of the many styles that matplotlib offers, 
#and change the style your graphs use to that one

#5) Finally, decide which style format you prefer 
#(your’s or the new matplotlib one you chose), 
#go with that style and save your Figure, 
#giving it a distinct name so that you don’t 
#have to open it to know what the graph will show