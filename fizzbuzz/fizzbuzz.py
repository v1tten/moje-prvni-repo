number = 0 
while number < 30:
    number += 1
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
            print("Fizz")
    elif number % 5 == 0:
                print("Buzz")

    else:
        print(f"{number}")
    