import sys
import random

numWords = int(sys.argv[1])
dictFile = open(sys.argv[2],"r").read().split()

def groupWords(text):
    ourDict = {}
    group = []
    for w in text:
        if len(group) == numWords:
            if ourDict.get(tuple(group)) == None:
                ourDict[tuple(group)] = [w]
            else:
                ourDict[tuple(group)].append(w)
            group.append(w)
            group = group[1:]
        else:
            group.append(w)
    return ourDict

def markovMulti(numTimes,ourDict):
    outwords = []
    testGroup = []
    for i in range(0,numTimes):
        if(len(testGroup) < numWords):
            testGroup = list(random.choice(list(ourDict.keys())))
            outwords = list(testGroup)
        else:
            w = random.choice(ourDict[tuple(testGroup)])
            testGroup.append(w)
            testGroup = testGroup[1:]
            outwords.append(w)

    return " ".join(outwords)

d = groupWords(dictFile)

print(markovMulti(1000,d))
