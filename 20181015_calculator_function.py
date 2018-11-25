#program: multiplying calculator function, improved
'''This program is a simple calculator'''

def calculator():
    user_number1 = input("enter first whole number: ")
    operator = input("enter operator(+ or - or * or /): ")
    user_number2 = input("enter second whole number: ")

    if operator == "+":
        user_sum = int(user_number1)+int(user_number2)
        print(user_number1, "+", user_number2, "=", user_sum)

    elif operator == "-":
        user_diff = int(user_number1)-int(user_number2)
        print(user_number1, "-", user_number2, "=", user_diff)

    elif operator == "*":
        user_product = int(user_number1)*int(user_number2)
        print(user_number1, "*", user_number2, "=", user_product)

    elif operator == "/":
        user_quotient = int(user_number1)/int(user_number2)
        print(user_number1, "/", user_number2, "=", int(user_quotient))

    else:
        print("Invalid Operator")
    
calculator()

#print(user_number1, "*", user_number2, "=", user_product)
