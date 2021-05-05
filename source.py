
import requests
import pprint
import json
from random_word import RandomWords

#store the request in this r variable
url = "https://lingua-robot.p.rapidapi.com/language/v1/entries/en/"
#put what word you want to look up after en/
#r = RandomWords()
totalScore = 0
totalRounds = 0

headers = {
    'x-rapidapi-key': "5da15bccffmsh6b27a6ff8f3b2f8p152169jsn23a9f2be1883",
    'x-rapidapi-host': "lingua-robot.p.rapidapi.com"
    }


def getAntonymList(word):
    antonymList = []
    newURL = url+word
    response = requests.request("GET", newURL, headers=headers)
    data = response.json()


    if 'lexemes' in data['entries'][0]:
        if len(data['entries'][0]['lexemes']) > 0:
            for i in range((len(data['entries'][0]['lexemes']))):
                if 'antonymSets' in data['entries'][0]['lexemes'][i]:
                    for j in range((len(data['entries'][0]['lexemes'][i]['antonymSets']))):
                        for k in range((len(data['entries'][0]['lexemes'][i]['antonymSets'][j]['antonyms']))):
                            if isinstance(data['entries'][0]['lexemes'][i]['antonymSets'][j]['antonyms'][k], str):
                                antonymList.append(data['entries'][0]['lexemes'][i]['antonymSets'][j]['antonyms'][k])
    else:
        startRound()
    uniqueAntonymList = set(antonymList)
    #print(uniqueAntonymList)
    if len(uniqueAntonymList) == 0:
        return 0

    print(antonymList)
    return uniqueAntonymList


def intro():
    print("The object of this game is to correctly guess an antonym for a random word")
    print("Every correct answer will net you 1 point")
    print("Once you receive 5 points, you win")
    doesUserWanttoPlay = input("If you want to play, press any key, otherwise, exit the program")
    if doesUserWanttoPlay:
        startRound()


def verifyWordHasAntonym(word):
    antonymList = []
    newURL = url + word
    response = requests.request("GET", newURL, headers=headers)
    data = response.json()
    if 'lexemes' in data['entries'][0]:
        if len(data['entries'][0]['lexemes']) > 0:
            for i in range((len(data['entries'][0]['lexemes']))):
                if 'antonymSets' in data['entries'][0]['lexemes'][i]:
                    for j in range((len(data['entries'][0]['lexemes'][i]['antonymSets']))):
                        for k in range((len(data['entries'][0]['lexemes'][i]['antonymSets'][j]['antonyms']))):
                            if isinstance(data['entries'][0]['lexemes'][i]['antonymSets'][j]['antonyms'][k], str):
                                antonymList.append(data['entries'][0]['lexemes'][i]['antonymSets'][j]['antonyms'][k])
    else:
        startRound()
    uniqueAntonymList = set(antonymList)

    if len(uniqueAntonymList) > 0:
        return True

    else:
        return False


def userGuess(antonymset, theRandomWordGiven):
    global totalScore
    global totalRounds

    print("Guess an antonym for: "+theRandomWordGiven)
    userInput = input()
    if userInput in antonymset:
        print("Congratulations, that was correct\n")
        totalScore += 1
        totalRounds += 1
        startRound()

    else:
        print("Sorry, that was the wrong answer, try again.")
        totalRounds += 1
        startRound()


def startRound():
    global totalScore
    r = RandomWords()
    nextR = RandomWords()

    randomWord = r.get_random_word(hasDictionaryDef="true")

    if verifyWordHasAntonym(randomWord):
        userGuess(getAntonymList(randomWord), randomWord)
    else:
        startRound()



intro()
startRound()
