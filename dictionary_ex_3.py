# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Adding elements one at a time
Dict[0] = 'Basu'
Dict[2] = 'Dev'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)

# Adding Nested Key value to Dictionary
Dict[5] = {'Nested': {'1': 'Life', '2': 'Earth'}}
print("\nAdding a Nested Key: ")
print(Dict)

print("\nAccessing a element by using key: ")
print(Dict[5])
print(Dict['Value_set'])

print("\nAccessing a element using get:")
print(Dict.get(3))


print("\nAccessing a nested dictionary element: ")
print(Dict[5]['Nested']['1'])

Dict[6] = 'Basudev'
print("\nInitial Dictionary: ")
print(Dict)

# Deleting a Key value
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)

# Deleting a Key from
# Nested Dictionary
del Dict[5]['Nested']['1']
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)

print('Deleting a key using pop() method')
pop_ele = Dict.pop(2)
print('\nDictionary after deletion: ' + str(Dict))
print('Value associated to poped key is: ' + str(pop_ele))

# Creating Dictionary
Dict = {1: 'Java', 'Python': 'Ruby', 3: 'Scala', 0: 'Basu', 2: 'Welcome', 3: 1}

# Deleting an arbitrary key
# using popitem() function
print('\nbefore deletion'+str(Dict))
pop_ele = Dict.popitem()
print("\nDictionary after deletion: " + str(Dict))
print("The arbitrary pair returned is: " + str(pop_ele))

# Deleting entire Dictionary
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict)


