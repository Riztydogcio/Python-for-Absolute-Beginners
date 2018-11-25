#say "Hello" using nested if

say_hello = input('Say "Hello" y/n? ')

if say_hello.lower() == "y":
    print()
    print('Full "Hello"')
    full_hello = input("y/n? ")
    if full_hello.lower() == "y":
        print()
        print("Hello")
    elif full_hello.lower() == "n":
        print()
        print("Hi")

    elif full_hello.lower() != "y" or "n":
        print("Invalid answer")

elif say_hello.lower() == "n":
    print("Hi")

elif say_hello.lower() != "y" or "n":
    print("Invalid answer")

#nested if - testing for False

bird_name = "robin", "pigeon", "eagle", "dove", "kingfisher"
bird_guess = input("Enter guess (bird name): ")

if bird_guess.lower() in bird_name:
    print("Yes, 1st try!")
elif bird_guess.lower() not in bird_name:
    print("No, guess again")
    print()
    
    guess_2 = input("Enter guess: ")
    if guess_2.lower() in bird_name:
        print("Yes, 2nd try!")
        print()
    elif guess_2.lower() not in bird_name:
        print("No, guess again")
        print()
        
        guess_3 = input("Enter guess: ")
        if guess_3.lower() in bird_name:
            print("Yes, 3rd try!")
        elif guess_3.lower() not in bird_name:
            print ("Sorry, out of tries")
