string = input("please enter your own string:")
string2 = ('')
for i in string:
    string2 = i + string2
    print("\nthe orininal string = ", string)
print("the reversed string = ", string2)