myString = "Hello, World!"

print(myString.index('o'))
print(myString.count('l'))
print(myString[3:7])

# You can even put negative numbers inside the brackets.
# They are an easy way of starting at the end of the string instead of the beginning.
# This way, -3 means "3rd character from the end".
# Last is option is step.
# [start:stop:step]
print(myString[-3::1])

# Reversing a string using the same method
myReversedString = myString[::-1]
print(myReversedString)

print(myString.upper())
print(myString.lower())

print(myString.split(" "))
