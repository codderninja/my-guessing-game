print("please enter your name")
name=str(input())
n=25
number_of_guesses=1
print("You have 9 chance ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<25:
        print("Answer is higher than", guess_number)
    elif guess_number>25:
        print("Answer is smaller than ", guess_number)
    else:
        print(name,  "is the winner\n")
        print("you finish the game in", number_of_guesses, "chance")
        break
    print(9-number_of_guesses,"chance left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")
  

