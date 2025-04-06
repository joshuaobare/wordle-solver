import random
import enchant
import time

dictionary = enchant.Dict("en_US")

word = input("Input word with spaces\t")
letterArray = input("Type in letters\t")
letters = list(letterArray)
mustHaveLetters = input("Must have?\t")
mustHave = list(mustHaveLetters)
dictionary = enchant.Dict("en_US")

words = []
start_time = time.time()
for y in range((len(letters))**5):
    wordCopy = []
    for x in range(len(word)):
        if word[x] == " ":
            wordCopy.append(random.choice(letters))
        else:
            wordCopy.append(word[x])    
    
    checksOut = dictionary.check("".join(wordCopy)) 
    if checksOut:
        words.append("".join(wordCopy))  
        
finalWords = []

for l in words:
    present = True
    
    for r in mustHave:
        if r not in l:
            present = False
    
    if present:
        print(l)
        finalWords.append(l)
    
        
with open("words.txt", "w", encoding="utf-8" , newline = "") as file:
    for n in list(set(finalWords)):
        file.write(n + "\n")
        
        
print("--- %s seconds ---" % (time.time() - start_time))
