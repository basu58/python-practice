smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
for n in "banana":
    print(n)
str = "Hello Python"
print(str[6:len(str)])
print(len(str))
word = "bananana"
i = word.find("na")
print(i)
print(dir(word))