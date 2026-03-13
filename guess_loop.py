


def int_check(question, low=None, high=None, exit_code=None): 
    
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")
        
    else:
        error = (f"Please enter an integer that"
                 f"is between {low} and {high} (inclusive)")
        
    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            if low is not None and response < low:
                print(error)

            elif high is not None and response > high:
                print(error)

            else:
                return response

        except ValueError:
            print(error)





secret = 7


low_num = 0
high_num = 10
guesses_allowed = 5

guesses_used = 0
already_guessed = []


guess = ""
while guess != secret and guesses_used < guesses_allowed:
    
    guess = int_check("Guess: ", low_num, high_num)

    if guess == "xxx":
        end_game = "yes"
        break


    if guess in already_guessed:
        print(f"You've already guessed {guess}. You still have "
              f"{guesses_allowed - guesses_used} / {guesses_allowed} guesses")
        continue

    else:
        already_guessed.append(guess)


    guesses_used += 1


    if guess < secret and guesses_used < guesses_allowed:
        feedback = (f"Too low, try a higher number. "
                    f"You have {guesses_allowed - guesses_used} / {guesses_allowed} guesses left")

        print(feedback)

    elif guess > secret and guesses_used < guesses_allowed:
        feedback = (f"Too high, try a lower number. "
                    f"You have {guesses_allowed - guesses_used} / {guesses_allowed} guesses left")
        print(feedback)


    elif guess == secret:
        if guesses_used == 1:
            feedback = "Wow, you got lucky. You got it on your first guess"
        elif guesses_used == guesses_allowed:
            feedback = f"Phew! You got it in {guesses_used} guesses."
        else:
            feedback = f"Well done! You guessed the secret number in {guesses_used} guesses."

    else:
        feedback = "You have no more guesses. You lost the round!"

    if guesses_used == guesses_allowed - 1:
        print("Careful, you only have one guess left!")

print()
print(feedback)
print()
print("End of round.")
print()

        
        