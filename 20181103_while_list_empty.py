dog_types = ["Lab", "Pug", "Poodle"]
print(dog_types, "\n")

#while dog_types:
    #print(dog_types.pop(), "popped, list now =", dog_types)
    #stops when list is empty

# delete a specific object from a list
if "Pug" in dog_types:
    dog_types.remove("Pug")
else:
    print("No Pug found")

print(dog_types)

# create an empty list
purchase_amounts = []

while True:
    user_input = input("enter price of items or type 'done' to finish: ")
    if user_input.isdigit():
        purchase_amounts += [user_input]

    elif user_input == "done":
        break

    else:
        print(user_input, "is not a valid amount")
print("purchase amount:", "\n", purchase_amounts)

# create a subtotal variable
subtotal = 0

while purchase_amounts:# loops while list is not empty
    value = purchase_amounts.pop() # pops last item in the list
    subtotal += float(value) # adds the last item in the list to subtotal

print("subtotal:", "\n", subtotal)


