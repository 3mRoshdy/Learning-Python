myList = [1, 2, 3]
print(myList)

myList.append(4)

for number in myList:
    print('number %d' % number)

evenNumbers = [2,4,6,8]
oddNumbers = [1,3,5,7]
allNumber = oddNumbers + evenNumbers

print(allNumber)

x = object()

x_ten_times = [x] * 10
print('x_ten_times list has %d number of x' % len(x_ten_times))

myList = [1,2,3]
print("A list: %s, and the list length is %d" % (myList, len(myList)))

# %s - String (or any object with a string representation, like numbers)
#
# %d - Integers
#
# %f - Floating point numbers
#
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#
# %x/%X - Integers in hex representation (lowercase/uppercase)
