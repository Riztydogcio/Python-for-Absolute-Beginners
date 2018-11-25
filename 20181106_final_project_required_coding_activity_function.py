#program: adding_report() function

def adding_report(report = "T"):
    total = 0 # initialize variables inside the function to avoid using the keyword global
    items =""
    while True:
        user_input = input("Enter an integer or \"Q\" to quit: ")
        if user_input.isdigit():
            total += int(user_input)
            if report.upper() == "A":
                items += user_input + "\n"

        elif user_input.upper() == "Q":
            if report.upper() == "A":
                print("\nItems\n" + str(items[0:]))
                print("Total\n" + str(total))
                break
            elif report.upper() == "T":
                print("\nTotal\n" + str(total))
                break

        else:
            print(user_input, "is invalid input")

adding_report("A") # calls the function that prints the items and the total
adding_report("T") # calls the function that prints only the total

