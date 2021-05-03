This is a README for antonym guesser
The game will start with the user being given a random word.
The user will have to guess an antonym for the given word.
The user given antonym must be on the approved list of antonyms given by a dictionary
Rounds end after a user submits a word.
The user is awarded one point if they correctly give an antonym on the approved list
The user will not be awarded any points if their word is not on the approved list
The user will play until they reach a score of 5
The user's overall score will be determined on the number of rounds it took them to finish

Side notes:
Not all words have antonyms
If a word does have an antonym, its under entries>entry>lexemes>antonymsets>antonyms
Api would sometimes append a single object list, as a result not able to turn antonymList into a set of unique antonyms, as you cannot turn a list into a set if the list contains a list