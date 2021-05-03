
import requests
import pprint
import json
from random_word import RandomWords

#store the request in this r variable
url = "https://lingua-robot.p.rapidapi.com/language/v1/entries/en/"
#put what word you want to look up after en/
#r = RandomWords()
totalScore = 0

headers = {
    'x-rapidapi-key': "5da15bccffmsh6b27a6ff8f3b2f8p152169jsn23a9f2be1883",
    'x-rapidapi-host': "lingua-robot.p.rapidapi.com"
    }

#response = requests.request("GET", url, headers=headers)

#pprint.pprint(response.json()['entries'][0]['lexemes'][0]['antonymSets'][0])
#.pprint(response.json())

'''
data = response.json()
antonymList = []

for i in range((len(data['entries'][0]['lexemes']))):
    if 'antonymSets' in data['entries'][0]['lexemes'][i]:
        for j in range((len(data['entries'][0]['lexemes'][i]['antonymSets']))):
            for k in range((len(data['entries'][0]['lexemes'][i]['antonymSets'][j]['antonyms']))):
                if isinstance(data['entries'][0]['lexemes'][i]['antonymSets'][j]['antonyms'][k], str):
                    antonymList.append(data['entries'][0]['lexemes'][i]['antonymSets'][j]['antonyms'][k])

            #print(data['entries'][0]['lexemes'][i]['antonymSets'][j]['antonyms'])
        #antonymList.append(data['entries'][0]['lexemes'][i]['antonymSets'])
        
        print(antonymList)
        uniqueAntonymList = set(antonymList)
        
'''


def getAntonymList(word):
    antonymList = []
    newURL = url+word
    response = requests.request("GET", newURL, headers=headers)
    data = response.json()
    for i in range((len(data['entries'][0]['lexemes']))):
        if 'antonymSets' in data['entries'][0]['lexemes'][i]:
            for j in range((len(data['entries'][0]['lexemes'][i]['antonymSets']))):
                for k in range((len(data['entries'][0]['lexemes'][i]['antonymSets'][j]['antonyms']))):
                    if isinstance(data['entries'][0]['lexemes'][i]['antonymSets'][j]['antonyms'][k], str):
                        antonymList.append(data['entries'][0]['lexemes'][i]['antonymSets'][j]['antonyms'][k])

    uniqueAntonymList = set(antonymList)
    print(uniqueAntonymList)
    #if len(uniqueAntonymList) == 0:
    return uniqueAntonymList


def intro():
    print("The object of this game is to correctly guess an antonym for a random word")
    print("Every correct answer will net you 1 point")
    print("Once you receive 5 points, you win")
    doesUserWanttoPlay = input("If you want to play, press any key, otherwise, exit the program")
    if doesUserWanttoPlay:
        startGame()


def startGame():
    global totalScore
    r = RandomWords()
    nextR = RandomWords()

    randomWord = r.get_random_word(hasDictionaryDef="true")
    getAntonymList(randomWord)
    guess = input("Guess an antonym for: "+randomWord)
    if guess in getAntonymList(randomWord):
        print("Congratulations, you earned a point!")
        totalScore += 1
    else:
        print("Sorry, that was wrong, try again with the next word")
        nextRandomWord = nextR.get_random_word(hasDictionaryDef="true")
        getAntonymList(nextRandomWord)

''' Old getAntonymList def
def getAntonymList(word):
    newURL = url+word
    response = requests.request("GET", newURL, headers=headers)
    data = response.json()['entries'][0]['lexemes'][0]['antonymSets'][0]
    responseDictionary = json.loads(response.json())
    print(responseDictionary)
    #print(data)
'''
intro()
startGame()