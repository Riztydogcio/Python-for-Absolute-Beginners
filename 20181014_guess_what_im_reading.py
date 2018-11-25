# program guess what I'm reading

can_read = input("enter 1 word describing something that can be read: ")
can_read_things = input("enter 3 items that can be read: ")

if can_read in can_read_things:
    print("item found = True")
else:
    print("item not found = False")
