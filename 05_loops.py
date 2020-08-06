numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    print("number is %d" % num)

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# using 'range' for setting the range for the iteration
for num in range(3,6):
    pass

count = 0
while count < 4:
    count += 1

# 'break' is used to exit a for loop or a while loop,
# whereas continue is used to skip the current block,
# and return to the "for" or "while" statement.

# 'else' can be used with loops when conditions to enter the
# interations fails.
count = 0
while count > 5:
    pass
else:
    print('count was less than 5')
