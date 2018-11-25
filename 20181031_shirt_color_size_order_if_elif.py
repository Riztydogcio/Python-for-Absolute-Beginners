#program: shirt order
available_colors = "white, blue"
white_size = "L, M"
blue_size = "S, M"

shirt_color = input("Order shirt color (White/Blue): ")

if shirt_color.lower() in available_colors: #did not follow instruction in the activity to set a "variable = False" before nested if
    print(shirt_color.title(), "is available")

    #checks user input if white, then proceeds to check size available for white
    if shirt_color.lower() == "white":
        shirt_size = input("Choose shirt size (L/M) for " + shirt_color.lower() + " shirt: ")
        if shirt_size.upper() in white_size:
            print("Your shirt order color", shirt_color.title(), "size", shirt_size.upper(), "has been received")
        else:
            print("Sorry size", shirt_size.upper(), "is not available for", shirt_color.lower())

    #checks user input is blue, then proceeds to check available sizes in blue
    elif shirt_color.lower() == "blue":
        shirt_size = input("Choose shirt size (M/S) for " + shirt_color.lower() + " shirt: ")
        if shirt_size.upper() in blue_size:
            print("Your shirt order color", shirt_color.title(), "size", shirt_size.upper(), "has been received")
        else:

            print("Sorry size", shirt_size.upper(), "is not available for", shirt_color.lower())

#if input is neither white nor blue, prints unavailability
else:
    print("Sorry", shirt_color, "is not available. \ncomeback tomorrow.")


#go back to IMG_1790.PNG to review code following instruction to set "available = False"
