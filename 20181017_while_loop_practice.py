#this example never loops because the break has no conditions
while True:
    print("write forever, unless there is a \"break\"")
    break

#review the NUMBER GUESS code then run - Q. What cause the break statement to run?

number_guess = "0"
secret_number = "5"

while True:
    number_guess = input("guess the number 1 to 5: ")
    if number_guess == secret_number:
        print("Yes", number_guess, "is correct!\n")
        break
    else:
        print(number_guess, "is incorrect\n")
