# External module imports
#import RPi.GPIO as GPIO
import time

aWords = []
bWords = []
cWords = []
dWords = []
eWords = []
fWords = []
gWords = []
hWords = []
iWords = []
jWords = []
kWords = []
lWords = []
mWords = []
nWords = []
oWords = []
pWords = []
qWords = []
rWords = []
sWords = []
tWords = []
uWords = []
vWords = []
wWords = []
xWords = []
yWords = []
zWords = []

#global vars used for computing
topChar = ""
midChar = ""
lowChar = ""
forChar = ""
fivChar = ""
sixChar = ""
sevChar = ""
eigChar = ""
ninChar = ""

#simple file reading
def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    return words

#assigns the dictionary to a list in order to optimize it 
def createSortedList(listToSort):
    for val in reversed(listToSort):
        if(val[0].lower() == "a"):
            aWords.append(val+" ")
        if(val[0].lower() == "b"):
            bWords.append(val+" ")
        if(val[0].lower() == "c"):
            cWords.append(val+" ")
        if(val[0].lower() == "d"):
            dWords.append(val+" ")
        if(val[0].lower() == "e"):
            eWords.append(val+" ")
        if(val[0].lower() == "f"):
            fWords.append(val+" ")
        if(val[0].lower() == "g"):
            gWords.append(val+" ")
        if(val[0].lower() == "h"):
            hWords.append(val+" ")
        if(val[0].lower() == "i"):
            iWords.append(val+" ")
        if(val[0].lower() == "j"):
            jWords.append(val+" ")
        if(val[0].lower() == "k"):
            kWords.append(val+" ")
        if(val[0].lower() == "l"):
            lWords.append(val+" ")
        if(val[0].lower() == "m"):
            mWords.append(val+" ")
        if(val[0].lower() == "n"):
            nWords.append(val+" ")
        if(val[0].lower() == "o"):
            oWords.append(val+" ")
        if(val[0].lower() == "p"):
            pWords.append(val+" ")
        if(val[0].lower() == "q"):
            qWords.append(val+" ")
        if(val[0].lower() == "r"):
            rWords.append(val+" ")
        if(val[0].lower() == "s"):
            sWords.append(val+" ")
        if(val[0].lower() == "t"):
            tWords.append(val+" ")
        if(val[0].lower() == "u"):
            uWords.append(val+" ")
        if(val[0].lower() == "v"):
            vWords.append(val+" ")
        if(val[0].lower() == "w"):
            wWords.append(val+" ")
        if(val[0].lower() == "x"):
            xWords.append(val+" ")
        if(val[0].lower() == "y"):
            yWords.append(val+" ")
        if(val[0].lower() == "z"):
            zWords.append(val+" ")

#returns the appropiate list based on the charEntered, returns a list made in listSorter
def getSortedList(charEntered):
    global aWords
    global bWords
    global cWords
    global dWords
    global eWords
    global fWords
    global gWords
    global hWords
    global iWords
    global jWords
    global kWords
    global lWords
    global mWords
    global nWords
    global oWords
    global pWords
    global qWords
    global rWords
    global sWords
    global tWords
    global uWords
    global vWords
    global wWords
    global xWords
    global yWords
    global zWords

    charEntered = charEntered[0]

    if(charEntered.lower() == "a"):
        return aWords
    if(charEntered.lower() == "b"):
        return bWords 
    if(charEntered.lower() == "c"):
        return cWords
    if(charEntered.lower() == "d"):
        return dWords 
    if(charEntered.lower() == "e"):
        return eWords
    if(charEntered.lower() == "f"):
        return fWords 
    if(charEntered.lower() == "g"):
        return gWords
    if(charEntered.lower() == "h"):
        return hWords 
    if(charEntered.lower() == "i"):
        return iWords
    if(charEntered.lower() == "j"):
        return jWords 
    if(charEntered.lower() == "k"):
        return kWords
    if(charEntered.lower() == "l"):
        return lWords 
    if(charEntered.lower() == "m"):
        return mWords
    if(charEntered.lower() == "n"):
        return nWords 
    if(charEntered.lower() == "o"):
        return oWords
    if(charEntered.lower() == "p"):
        return pWords
    if(charEntered.lower() == "q"):
        return qWords
    if(charEntered.lower() == "r"):
        return rWords 
    if(charEntered.lower() == "s"):
        return sWords
    if(charEntered.lower() == "t"):
        return tWords 
    if(charEntered.lower() == "u"):
        return uWords
    if(charEntered.lower() == "v"):
        return vWords 
    if(charEntered.lower() == "w"):
        return wWords
    if(charEntered.lower() == "x"):
        return xWords 
    if(charEntered.lower() == "y"):
        return yWords
    if(charEntered.lower() == "z"):
        return zWords 

#creates an array nextChars of the next possible chars based on the word entered
def getPossibleNextChars(wordToCompare):
    nextChars = []
    currentWordLength = len(wordToCompare)
    basisList = getSortedList(wordToCompare)


    for val in basisList:
        stringLength = len(val)
        if(stringLength >= currentWordLength+1 and (val[0:currentWordLength] == wordToCompare)):
            nextChars.append(val[currentWordLength])

    return nextChars 

#returns a list of words/segments that exist in the dictionary based on wordToCompare
def getPossibleWords(wordToCompare):
    possibleWords = []
    currentWordLength = len(wordToCompare)
    basisList = getSortedList(wordToCompare)

    for val in basisList:
        stringLength = len(val)
        if(stringLength >= currentWordLength and (val[0:currentWordLength] == wordToCompare)):
            possibleWords.append(val)

    return possibleWords 

#assigns topChar, midChar, and lowChar
def getCommonListVals(basisList):
    global topChar
    global midChar
    global lowChar
    global forChar
    global fivChar
    global sixChar
    global sevChar
    global eigChar
    global ninChar

    tmpList = list(basisList)

    if(len(tmpList)):
        topChar = max(set(tmpList), key = tmpList.count)
        for val in reversed(tmpList):
            if(val == topChar):
                tmpList.remove(val)
    else:
        topChar = ""

    if(len(tmpList)):
        midChar = max(set(tmpList), key = tmpList.count)
        for val in reversed(tmpList):
            if(val == midChar):
                tmpList.remove(val)
    else:
        midChar = ""

    if(len(tmpList)):
        lowChar = max(set(tmpList), key = tmpList.count)
        for val in reversed(tmpList):
            if(val == lowChar):
                tmpList.remove(val)
    else:
        lowChar = ""
    
    if(len(tmpList)):
        forChar = max(set(tmpList), key = tmpList.count)
        for val in reversed(tmpList):
            if(val == forChar):
                tmpList.remove(val)
    else:
        forChar = ""

    if(len(tmpList)):
        fivChar = max(set(tmpList), key = tmpList.count)
        for val in reversed(tmpList):
            if(val == fivChar):
                tmpList.remove(val)
    else:
        fivChar = ""

    if(len(tmpList)):
        sixChar = max(set(tmpList), key = tmpList.count)
        for val in reversed(tmpList):
            if(val == sixChar):
                tmpList.remove(val)
    else:
        sixChar = ""

    if(len(tmpList)):
        sevChar = max(set(tmpList), key = tmpList.count)
        for val in reversed(tmpList):
            if(val == sevChar):
                tmpList.remove(val)
    else:
        sevChar = ""

    if(len(tmpList)):
        eigChar = max(set(tmpList), key = tmpList.count)
        for val in reversed(tmpList):
            if(val == eigChar):
                tmpList.remove(val)
    else:
        eigChar = ""

    if(len(tmpList)):
        ninChar = max(set(tmpList), key = tmpList.count)
    else:
        ninChar = ""

#returns 1 if current word exists in a words list, 0 if it does not
def existsInDictionary(wordToCompare, wordList):
    currentWordLength = len(wordToCompare)

    for value in wordList:
        if(wordToCompare == value[0:currentWordLength]):
            return 1

    return 0

#returns status code of inputted text
def probabilityDetector(wordToCompare, wordList, elapsedTime):
    topCharDelay = 1.3
    midCharDelay = 1.5
    lowCharDelay = 1.7
    forCharDelay = 1.9
    fivCharDelay = 2.1
    sixCharDelay = 2.3
    sevCharDelay = 2.5
    eigCharDelay = 2.8
    ninCharDelay = 3.1

    possCharDelay = 1.5

    tooFastDelay = 0.3
    tooSlowDelay = 1

    if(elapsedTime >= tooFastDelay):
        if((topChar == wordToCompare[-1]) and (elapsedTime < possCharDelay)):
            print("Probability: 100%")
            if(wordToCompare[-1] == " "):
                print("space entered")
                return 101
            return(100)
        elif(midChar == wordToCompare[-1] and (elapsedTime < possCharDelay)):
            print("Probability: 90%")
            if(wordToCompare[-1] == " "):
                print("space entered")
                return 101
            return(85)
        elif(lowChar == wordToCompare[-1] and (elapsedTime < possCharDelay)):
            print("Probability: 80%")
            if(wordToCompare[-1] == " "):
                print("space entered")
                return 101
            return(70)
        elif(forChar == wordToCompare[-1] and (elapsedTime < possCharDelay)):
            print("Probability: 70%")
            if(wordToCompare[-1] == " "):
                print("space entered")
                return 101
            return(55)
        elif(fivChar == wordToCompare[-1] and (elapsedTime < possCharDelay)):
            print("Probability: 60%")
            if(wordToCompare[-1] == " "):
                print("space entered")
                return 101
            return(40)
        elif(sixChar == wordToCompare[-1] and (elapsedTime < possCharDelay)):
            print("Probability: 50%")
            if(wordToCompare[-1] == " "):
                print("space entered")
                return 101
            return(20)
        elif(sevChar == wordToCompare[-1] and (elapsedTime < possCharDelay)):
            print("Probability: 40%")
            if(wordToCompare[-1] == " "):
                print("space entered")
                return 101
            return(55)
        elif(eigChar == wordToCompare[-1] and (elapsedTime < possCharDelay)):
            print("Probability: 30%")
            if(wordToCompare[-1] == " "):
                print("space entered")
                return 101
            return(40)
        elif(ninChar == wordToCompare[-1] and (elapsedTime < possCharDelay)):
            print("Probability: 20%")
            if(wordToCompare[-1] == " "):
                print("space entered")
                return 101
            return(20)
        elif(existsInDictionary(wordToCompare, wordList)):
            print("Probability: 10%")
            if(wordToCompare[-1] == " "):
                print("space entered")
                return 101
            return(10)
        elif(len(wordToCompare) == 1):
            print("Probability: New word, so idk")
            if(wordToCompare[-1] == " "):
                print("space entered")
                return 101
            return(102)
        #elif(existsInDictionary(wordToCompare, wordList)):
            #print("Probability: 5%")
            #if(wordToCompare[-1] == " "):
                #print("space entered")
                #return 101
            #return(5)
        else:
            print("Probability: 0% - A TYPO WAS MADE")
            return(0)
    else:
        print("You are typing too fast, slow down")
        return(0)
    

#def keyDriver(codeRecieved, currentWord)
    #start a timer

    #if((codeRecieved == 100) and (topCharDelay))
    


#main driver
dictionary = readFile("basic_words.txt")
createSortedList(dictionary)
currentWord = ""
while(1):
    startTime = time.time()
    keyInput = input("\nEnter key from keyboard:") #for python 2.0 use raw_input()
    endTime = time.time()

    elapsedTime = endTime - startTime

    currentWord = currentWord + keyInput

    

    nextCharsList = getPossibleNextChars(currentWord)
    possibleWordsList = getPossibleWords(currentWord)
    codeRecieved = probabilityDetector(currentWord, possibleWordsList, elapsedTime)
    getCommonListVals(nextCharsList)

    if(codeRecieved == 0):
        currentWord = currentWord[:-1]
    elif(codeRecieved == 101):
        currentWord = ""
        #print("sending the space bar")
    #telse:
        #print("I am sending the letter " + currentWord[-1] + " to the PC")

    #print(topChar)
    #print(midChar)
    #print(lowChar)
    #print(forChar)
    #print(fivChar)
    #print(sixChar)
    #print(sevChar)
    #print(eigChar)
    #print(ninChar)
    print("THE CURRENT WORD IS: "+currentWord)
    