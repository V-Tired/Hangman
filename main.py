game = True
while game:

    import random
    from hangman_words import word_list

    stages = [" ", "<3", "<3<3", "<3<3<3", "<3<3<3<3", "<3<3<3<3<3"]
    chosen_word = random.choice(word_list)
    lives = 6
    i = len(chosen_word)
    display = []
    incorrect_guess = []

    input("Welcome to Hangman! Click enter to continue. \n")

    print(f"The word has {i} letters.")
    for letter in chosen_word:
        display += "_"
    print(f"{''.join(display)}")

    while "_" in display and lives > 0:

        print(f"Incorrect letters guessed: {incorrect_guess}")
        print(f"You have {lives} more guesses.")
        guess = input("Choose a letter.\n").lower()

        if guess in display:
            print("You have already chosen that letter.")

        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(f"{''.join(display)}")

        if guess not in chosen_word:
            lives -= 1
            print(f"{guess} is not in this word.")
            incorrect_guess += guess

    print(f"Letters guessed: {incorrect_guess}")
    print(f"{''.join(display)}")

    if lives == 0:
        print(f"You lose. The word was {chosen_word}.")
    else:
        print("You Win!")

    replay = input("Do you want to play again, Y or N?\n").upper()
    if replay == "Y":
        game = True
    elif replay == "N":
        game = False
