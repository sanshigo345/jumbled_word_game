import sys, time

if len(sys.argv) != 3:
    print("You must write two arguments for this program to work!")
    exit()

f1_name = sys.argv[1]
f2_name = sys.argv[2]

f1 = open(f1_name, encoding="utf-8-sig")
f2 = open(f2_name, encoding="utf-8-sig")

jumblewords = {}
for line in f1:
    key, values = line.split(":")
    values = values.strip()
    values = values.split(",")
    jumblewords[key] = values
f1.close()

letter_values = {}
for line in f2:
    key, values = line.split(":")
    values = int(values.strip())
    letter_values[key] = values
f2.close()

def calcscore(list):
    def splitword(word):
        return [char for char in word]
    score = 0
    for item in list:
        splitword(item)
        for letter in item:
            score = score + (letter_values.get(letter.upper())*len(item))
    return score

counter = -1
turn_time = 30
for key in jumblewords.keys():
    counter = counter + 1
    print("Shuffled letters are: ", key.replace("I", "ı").replace("İ", "i").lower(), " Please guess words for these letters with minumum three letters")
    guessed_words = []
    start_time = time.time()
    elapsed_time = time.time() - start_time
    while elapsed_time < turn_time:
        playerguess = input("Guessed Word: ").replace("i","İ").upper()
        elapsed_time = time.time() - start_time
        if elapsed_time > turn_time:
            print("Sorry time is up, can not accept your last guess")
        else:
            if playerguess in jumblewords[key]:
                if playerguess in guessed_words:
                    print("You already guessed this word. ", end="")
                else:
                    guessed_words.append(playerguess)
                    print("Correct Guess! ", end="")
            else:
                print("Your guess is NOT a valid word. ", end="")
            print("You have", int(turn_time - elapsed_time), "seconds")
    calcscore(guessed_words)
    print("Score for {} is".format(list(jumblewords.keys())[counter]), calcscore(guessed_words), "and correct guessed words are:",
          "-".join(guessed_words).replace("I", "ı").replace("İ", "i").lower())
