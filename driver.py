# External module imports
#import RPi.GPIO as GPIO
import time
import json

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


#these two letters are used to determine the time needed for a new letter
nextPossibleLetter = ""
possibilityCheckVal = ""
nextChars = []
newWords = []
stalled = 0

iterativeNum = -1
currentWord = ""
listToWorkWith = []

#simple file reading
def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    return words

#assigns the dictionary to a list in order to optimize it 
def listSorter(listToSort):
    for val in reversed(listToSort):
        if(val[0].lower() == "a"):
            aWords.append(val)
        if(val[0].lower() == "b"):
            bWords.append(val)
        if(val[0].lower() == "c"):
            cWords.append(val)
        if(val[0].lower() == "d"):
            dWords.append(val)
        if(val[0].lower() == "e"):
            eWords.append(val)
        if(val[0].lower() == "f"):
            fWords.append(val)
        if(val[0].lower() == "g"):
            gWords.append(val)
        if(val[0].lower() == "h"):
            hWords.append(val)
        if(val[0].lower() == "i"):
            iWords.append(val)
        if(val[0].lower() == "j"):
            jWords.append(val)
        if(val[0].lower() == "k"):
            kWords.append(val)
        if(val[0].lower() == "l"):
            lWords.append(val)
        if(val[0].lower() == "m"):
            mWords.append(val)
        if(val[0].lower() == "n"):
            nWords.append(val)
        if(val[0].lower() == "o"):
            oWords.append(val)
        if(val[0].lower() == "p"):
            pWords.append(val)
        if(val[0].lower() == "q"):
            qWords.append(val)
        if(val[0].lower() == "r"):
            rWords.append(val)
        if(val[0].lower() == "s"):
            sWords.append(val)
        if(val[0].lower() == "t"):
            tWords.append(val)
        if(val[0].lower() == "u"):
            uWords.append(val)
        if(val[0].lower() == "v"):
            vWords.append(val)
        if(val[0].lower() == "w"):
            wWords.append(val)
        if(val[0].lower() == "x"):
            xWords.append(val)
        if(val[0].lower() == "y"):
            yWords.append(val)
        if(val[0].lower() == "z"):
            zWords.append(val)

#returns the list needed based on the char entered
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

#returns the most likely char from the list of words
def getPossibleNextChar(charEntered, curWord):
    global dictionary
    global iterativeNum
    global newWords
    global nextChars
    global listToWorkWith

    if(iterativeNum == -1):
        listToWorkWith = list(getSortedList(charEntered))

    del nextChars[:]

    iterativeNum+=1

    #loop in charge of deleting words that can't be typed
    #for index, val in reversed(list(enumerate(listToWorkWith))):
        #if(val[0:iterativeNum+1] == curWord):
            #print("\nit can possibly be the word " + val)

        #if(val[0:iterativeNum+1] != curWord):
            #print("\nI can assure you that you won't be typing in the word " + val)
            #listToWorkWith.pop(index)

    #loop in charge of assigning the next letter into a list
    for val in listToWorkWith:
        stringLength = len(val)
        if(stringLength > iterativeNum+1 and (val[0:iterativeNum+1] == currentWord)):
            #print(val + " is being compared with " + currentWord)
            nextChars.append(val[iterativeNum+1])
            

    if(len(nextChars)):
        return max(set(nextChars), key = nextChars.count)
    else:
        return "empty"





#if (nextPossibleKey == keyEntered)  then press key
#if (nextPossibleKey != keyEntered) and timePassed >= delay then let key pass through
#if (keyEntered d



#from here on forward is the main program
dictionary = readFile("basic_words.txt")
newWords = list(dictionary)
listSorter(newWords)

def possibilityCheck(charToCheck, nextChars):
    for value in nextChars:
        if(charToCheck == value):
            #print("hey, turns out that " + charToCheck + " is the same as " + value)
            return 1
    #print("hey, i returned zero")
    return 0

def actuationJudge(charToCheck, iterativeNum):
    global nextPossibleLetter
    global possibilityCheckVal
    global currentWord
    global stalled

    possibilityCheckVal = possibilityCheck(charToCheck, nextChars)

    if(iterativeNum != -1 and possibilityCheckVal == 0):
        print("Blocking this letter")
        #tmp = currentWord[:-1]
        #currentWord = tmp
        iterativeNum = iterativeNum -1
        #print("the current word is " + tmp)
    elif(charToCheck == nextPossibleLetter):
        print("This is very likely intentional")
        currentWord = currentWord + charToCheck
        nextPossibleLetter = getPossibleNextChar(charToCheck, currentWord)
    elif(charToCheck != nextPossibleLetter):
        print("Moderatately intentional")
        currentWord = currentWord + charToCheck
        nextPossibleLetter = getPossibleNextChar(charToCheck, currentWord)

    print("THE CURRENT WORD IS " + currentWord)



#keyboard autocorrect simulator
while(1):
    global iterativeNum
    global currentWord
    global newWords

    keyInput = raw_input("\nEnter key--------------------:")
    
    if(keyInput == " "):
        iterativeNum = -1
        currentWord = ""
        newWords = list(dictionary)

    else:
        #print("The next likely letter is " + autoCorrect(keyInput, currentWord) + " which is the one I would delay least")
        actuationJudge(keyInput, iterativeNum)
        #print("The most likely word you are going to type is " + getPossibleNextChar(keyInput, currentWord))

    #print("\n######## You currently have written: " + currentWord + " ########")