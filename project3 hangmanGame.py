import random
def hangman():
    word = random.choice(["pugger", "littlepugger", "superman", "thor", "pokemon", "avengers", "earth", "annabelle"])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessMade = ''

    while len(word)>0:
        main = ""
        #missed = 0
        for letter in word:
            if letter in guessMade:
                main = main + letter
            else:
                main = main + "_" + " "
        
        if main == word:
            print(main)
            print("You Win!")
            break

        print("Guess the word: ", main)
        guess=input()


        if guess in validLetters:
            guessMade = guessMade + guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            turns = turns - 1

            if turns == 9:
                print("9 terms left")
                print(" -------- ")
            if turns == 8:
                print("8 terms left")
                print(" -------- ")
                print("    O     ")
            if turns == 7:
                print("7 terms left")
                print(" -------- ")
                print("    O     ")
                print("    |     ")
            if turns == 6:
                print("6 terms left")
                print(" -------- ")
                print("    O     ")
                print("    |     ")
                print("   /      ")
            if turns == 5:
                print("5 terms left")
                print(" -------- ")
                print("    O     ")
                print("    |     ")
                print("   / \    ")
            if turns == 4:
                print("4 terms left")
                print(" -------- ")
                print("  \ O     ")
                print("    |     ")
                print("   / \    ")
            if turns == 3:
                print("3 terms left")
                print(" -------- ")
                print("  \ O /   ")
                print("    |     ")
                print("   / \    ")
            if turns == 2:
                print("2 terms left")
                print(" -------- ")
                print("  \ O /|  ")
                print("    |     ")
                print("   / \    ")
            if turns == 1:
                print("1 terms left")
                print("last breaths counting, take care")
                print(" -------- ")
                print("  \ O_/|  ")
                print("    |     ")
                print("   / \    ")
            if turns == 0:
                print("You Lose")
                print(" -------- ")
                print("    O_|   ")
                print("   /|\    ")
                print("   / \    ")
                break


name = input("Enter your name ")
print("Welcome ", name)
print("--------------")
print("Try to guess the word in less than 10 tries")
hangman()