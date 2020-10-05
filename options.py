## Script by almost_somebody ##

## Actual option values set in engine/options.json ##

import os
from os import path
import json

f = open(path.join("engine", "options.json"), "r")
dataValues = json.load(f)

def getSavePath():
    global dataValues
    savePath = dataValues['saveData']['filePath']
    saveName = dataValues['saveData']['fileName']
    newPath = path.join(savePath, saveName)
    return newPath

def getStartingRoom():
    global dataValues
    startingRoom = dataValues['defaultValues']['startingRoom']
    return startingRoom

def getWindowTitle():
    global dataValues
    windowTitle = dataValues['defaultValues']['windowTitle']
    return str(windowTitle)

def getWindowGeometry():
    global dataValues
    windowGeometry = dataValues['defaultValues']['windowGeometry']
    return windowGeometry

def getGameName():
    global dataValues
    gameName = dataValues['defaultValues']['gameName']
    return gameName