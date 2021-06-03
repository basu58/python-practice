x = [11, 1, 2, 5, 10, 3, 4]
large = small = x[0]
for i in x:
    if i > large:
        large = i
    elif i < small:
        small = i
print("small = "+str(small)+"\nlarge = "+str(large))
print("------------------------------------------------")
print("Max = "+str(max(x))+"\nMin = "+str(min(x)))

