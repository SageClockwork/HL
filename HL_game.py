import math
import random

# checks for an integer more than 0 (allows <enter>)

def yes_no(question):

    """Checks user responses to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Prints instructions"""

    print("""
                 *** Instructions ***

To begin, choose the number of rounds and either customise
the game parameters or go with the default game (where the 
secret number will be between 1 and 10).
          
Then choose how many rounds you'd like to play <enter> for
infinite mode.
          
Your goal is to try to guess the secret number without 
running out of guesses.
          
 Good Luck.
          
    """)

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

    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses

# main routine starts here
        
# Innitialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""


game_history = []
all_scores = []         

print()   
print("⬆️ ⬆️ ⬆️  Welcome to the Higher Lower Game ⬇️ ⬇️ ⬇️")
print()
        

want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()
        
# Ask the user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ", low=1, exit_code="")


if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

default_params = yes_no("Do you want to use the default game parameters? ")
if default_params == "yes":
    low_num = 0
    high_num = 10

else:   
    low_num = int_check("Low Number? ")
    high_num = int_check("High Number? ", low=low_num+1)


guesses_allowed = calc_guesses(low_num, high_num)
    
# Game loop starts here
while rounds_played < num_rounds and end_game=="no":

    # rounds headings
    if mode == "infinite":
        rounds_headings = f"\n=== Round {rounds_played + 1} (infinite mode) ==="
    else:
        rounds_headings = f"\n=== Round {rounds_played + 1} of {num_rounds} ==="

    print(rounds_headings)
    print()


    guesses_used = 0
    already_guessed = []

    secret = random.randint(low_num, high_num)
    print(secret)


    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:
        
        guess = int_check("Guess: ", low_num, high_num, "xxx")

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
            round_result = "won"
            history_item = f"Round: {rounds_played+1} - {round_result} in {guesses_used} guesse(s)"
            game_history.append(history_item)

            if guesses_used == 1:
                feedback = "Wow, you got lucky. You got it on your first guess"
            elif guesses_used == guesses_allowed:
                feedback = f"Phew! You got it on your last guess."
            else:
                feedback = f"Well done! You guessed the secret number in {guesses_used} guesses."

        else:
            round_result = "lost"
            history_item = f"Round: {rounds_played+1} - {round_result}"
            game_history.append(history_item)
            feedback = "You have no more guesses. You lost the round!"

            # penalise user for losing game
            guesses_used += 1

        if guesses_used == guesses_allowed - 1:
            print("Careful, you only have one guess left!")
        

        print()
        print(feedback)
        
    
    print()
    if end_game == "yes":
        break

    
    rounds_played += 1
    all_scores.append(guesses_used)
     

# Game loop ends here
         
# Game history / statistics area


if rounds_played > 0:

    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)
    

    print("\nStatistics")
    print(f"Best: {best_score} | Worst; {worst_score} | Average: {average_score:.2f} ")
    print()  



    see_history = yes_no("Do you want to see the game history? ")
    if see_history == "yes":
        print()
        print(game_history)
        print()

    
            




        

    
