numWords = 2
mostCommonWords = ["the","of","to","and","a","in","is","it","you","that"]

def addWord(d,group,word):
    if d.get(group) == None:
        d[group] = {word : 1}
    else:
        if d[group].get(word) == None:
            d[group][word] = 1
        else:
            d[group][word] = d[group][word] + 1

def makeOptions(options):
    result = []
    count = 0
    for w in options:
        result.append("!" + str(count) + ": " + w)
        count = count + 1
    return result

def getTopWords(d,ws):
    if d.get(ws) == None:
        return []
    else:
        opts = list(d.get(ws).items())
        opts.sort(key=lambda x: x[1])
        opts.reverse()
        return [p[0] for p in opts]

# this loop will continue until a command of !quit is given
def mainLoop():
    ourDict = {}
    textSoFar = []
    lastWords = []
    while True:
        options = []
        if len(lastWords) < numWords:
            options = mostCommonWords
        else:
            test = getTopWords(ourDict,tuple(lastWords))
            #we append to the options the most common words
            options = (test + mostCommonWords)[0:10]
        print("Your message: " + " ".join(textSoFar) + "\n")
        message = ("Choose from the following options with !#, !quit to exit, or type your own response\n"
                     +  " ".join(makeOptions(options)))
        choice = input(message + "\n")
        if choice[0] == '!':
            if choice == "!quit":
                break
            else:
                selectedWord = options[int(choice[1:])]
                if len(lastWords) == numWords:
                    addWord(ourDict,tuple(lastWords),selectedWord)
                    lastWords.append(selectedWord)
                    lastWords = lastWords[1:]
                else:
                    lastWords.append(selectedWord)
                textSoFar.append(selectedWord)
        else:
            if(len(lastWords) == numWords):
                addWord(ourDict,tuple(lastWords),choice)
                lastWords.append(choice)
                lastWords = lastWords[1:]
            else:
                lastWords.append(choice)
            textSoFar.append(choice)

mainLoop()
