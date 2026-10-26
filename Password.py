Password = "Password"
Attempts = 3

while True:
    Guess = input(":")

    if(Guess == Password):
        print("Correct")
        break
    else: 
        Attempts -= 1
        if(Attempts == 0):
            print("Ran out of guesses")
            break
        else:
            print(f"Remaining {Attempts} Attempts ")
        