#program: string analysis function

#the function returns a string message of an analysis of a test string passed as an arguent to the function

def str_analysis(analyze):
    if analyze.isdigit():
        if int(analyze) > 99:
            print(analyze, "is a pretty big number")
        elif int(analyze) < 99:
            print(analyze, "is a smaller number than expected")
    elif analyze.isalpha():
        print("\"" + analyze + "\"" + " is all aplhabetical characters!")
    else:
        print(analyze, "may have multiple character types")

user_input = ""

while user_input == "":
    user_input = input("enter word or integer: ")

str_analysis(user_input)

