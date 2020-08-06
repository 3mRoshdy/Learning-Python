phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

#[('Jill', 947662781), ('John', 938477566), ('Jack', 938377264)]
print(phonebook.items())
# {'Jill': 947662781, 'John': 938477566, 'Jack': 938377264}
print(phonebook)

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

del phonebook["Jill"]
