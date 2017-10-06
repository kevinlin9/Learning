import random
word_list = ["pizza", "tomato", "pepper", "gingersnap", "oreos"]
chosen_word = random.choice(word_list)
incorrect_guesses = 0
total_incorrect_allowed = 6
guessed_letters = []
while incorrect_guesses < total_incorrect_allowed:
    print()
    won = True
    for letter in chosen_word:
        if letter.upper() in guessed_letters:
            print(letter.upper(), end= ' ')
        else:
            won = False
            print("_ ", end=' ')

    print("\n\n You have %s incorrect guesses left. \n" %(total_incorrect_allowed - incorrect_guesses))
    if won:
        print("You have won!")
        exit()
    letter = input("Enter a single letter: ").replace(" ", "")
    if len(letter) > 1 or letter.upper() in guessed_letters:
        print("Bad input")
    elif letter.upper() in chosen_word.upper():
        print("%s is in the word!" % letter.upper())
    else:
        print("%s is not in the word!" % letter.upper())
        incorrect_guesses += 1
    guessed_letters.append(letter.upper())
print("You lost! The word was %s." %chosen_word)
