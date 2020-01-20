from PIL import Image
import statistics
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()



class Stamp:
    def __init__(self, country=None, region=None, year:int=None, faceValue:float=None, marketValue:float=None, image:Image=None):
        self.country = country
        self.region = region
        self.year = year
        self.faceValue = faceValue
        self.marketValue = marketValue
        self.image = image
        


    def listAttributes():
            for key in stampAttributes:
                 print(key.uppercase() + country)


class Coin:
    def __init__(self, country=None, region=None, year:int=None, faceValue:float=None, marketValue:float=None, image:Image=None):
        self.country = country
        self.region = region
        self.year = year
        self.faceValue = faceValue
        self.marketValue = marketValue
        self.image = image



##  Stamps ##
stampList = []

def addStamp():
    newStamp = Stamp(input("Country: "), input("Region: "), input("Year: "), input("Face Value: "), input("Market Value: "), Image.open(filedialog.askopenfilename()))
    stampList.append(newStamp)
    return newStamp




##  Coins ##
coinList = []

def addCoin():
    newCoin = Coin(input("Country: "), input("Region: "), input("Year: "), input("Face Value: "), input("Market Value: "), Image.open(filedialog.askopenfilename()))
    coinList.append(newCoin)
    return newCoin



## Methods ##
def stampSum():
    sum = 0
    for stamp in stampList:
        sum += float(stamp.marketValue)
    return sum

def coinSum():
    sum = 0
    for coin in coinList:
        sum += float(coin.marketValue)
    return sum

def totalSum():
    sum = 0
    sum += stampSum() + coinSum()
    return sum


def stampMedian():
    valueList = []
    for stamp in stampList:
        valueList.append(float(stamp.marketValue))
    print(statistics.median(valueList))

def stampMean():
    valueList = []
    for stamp in stampList:
        valueList.append(float(stamp.marketValue))
    print(statistics.mean(valueList))


def coinMedian():
    valueList = []
    for coin in coinList:
        valueList.append(float(coin.marketValue))
    print(statistics.median(valueList))

def coinMean():
    valueList = []
    for coin in coinList:
        valueList.append(float(coin.marketValue))
    print(statistics.mean(valueList))

def getStampAttributes(stamp:Stamp):
    
    thisStamp = {
        "Country": stamp.country,
        "Region": stamp.region,
        "Year": stamp.year,
        "FaceValue": stamp.faceValue,
        "MarketValue": stamp.marketValue,
        "Image": stamp.image
    }
    
    for attributeName, attributeValue in thisStamp.items():
        if attributeName == "Image":
            stamp.image.show()
        else:
            print(attributeName + " " + attributeValue)


def getCoinAttributes(coin:Coin):
    
    thisCoin = {
        "Country": coin.country,
        "Region": coin.region,
        "Year": coin.year,
        "FaceValue": stamcoin.faceValue,
        "MarketValue": coin.marketValue,
        "Image": coin.image
    }
    
    for attributeName, attributeValue in thisCoin.items():
        if attributeName == "Image":
            coin.image.show()
        else:
            print(attributeName + " " + attributeValue)

        
