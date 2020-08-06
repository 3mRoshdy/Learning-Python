def print_greetings():
    print('Hey there!')

def print_meetings_with_args(name, message):
    print("Hello there %s, this is from the function greeting you with the message: %s" % (name, message))

def sum_two_numbers(a,b):
    return a + b

print_meetings_with_args('Roshdy', 'Good Work')
sum = sum_two_numbers(1,2)
print(sum)
