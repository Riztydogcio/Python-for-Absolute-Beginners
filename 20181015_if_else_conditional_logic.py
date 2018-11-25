#age = input("enter age: ")
#if int(age) >= 12:
    #print("Age in 10 years is", int(age) + 10)
#else:
    #print("It's good to be", age)

def check_guess(letter, guess):
    guess = input("guess the letter: ").lower()
    if guess.isdigit() == True:
        print ("Invalid")
    elif guess == letter:
        print("Correct")
    elif guess > letter:
        print("Guess is high")
    else:
        print("Guess is low")

#check_guess("r", "r") '''calls the function'''
    
