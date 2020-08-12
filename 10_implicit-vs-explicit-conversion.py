'''
In Implicit type conversion, Python automatically converts one data type to another data type.
This process doesn't need any user involvement.
'''
num_int = 10
num_float = 12.3

num_new = num_int + num_float

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_float))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

'''
In Explicit Type Conversion, users convert the data type of an object to required data type.
We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion.
'''
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))
