# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Basu', 2: 'Dev', 3: 'Chhotaray'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Basu', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

# print keys as a list
print(list(Dict))
# print keys only
print(Dict.keys())
# print values only
print(Dict.values())
# print items
print(Dict.items())

print("\nTwo iteration values")
for i, j in Dict.items():
    print(i, j)
