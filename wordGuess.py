import random
print("Welcom! Let's play word guessing game!")

words = ["hello","nice","flawless","terrific","exquisite","cruel"]

word = random.choice(words)     #randomly select one of the words from the list of words
turns = 10
guesses = ''
while turns>0:
    #counts the no. of times user fails
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("\nYou win")
        print("\nThe word is:",word)
        break
    
    guess = input("\nenter a character: ")
    
    guesses += guess
    if guess not in word:
        print("\nWrong")
        turns -= 1
        print("\nYou have ",+ turns ,"more guesses")
        if turns == 0:
            print("\nYou loose!")




