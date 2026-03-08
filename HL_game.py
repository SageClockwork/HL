
# checks for an integer more than 0 (allows <enter>)
def int_check(question):
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


# main routine starts here
        
# Innitialise game variables
mode = "regular"
rounds_played = 0
            
            
print("🪨📄✂ Rock / Paper / Scissors Game ✂📄🪨")
print()
        
# Instructions
        
# Ask the user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5
        
# Game loop starts here
while rounds_played < num_rounds:

    # rounds headings
    if mode == "infinite":
        rounds_headings = f"\n=== Round {rounds_played + 1} (infinite mode) ==="
    else:
        rounds_headings = f"\n=== Round {rounds_played + 1} of {num_rounds} ==="

    print(rounds_headings)
    print()

    user_choice = input("Choose: ")

    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1
     

# Game loop ends here
        
# Game history / statistics area