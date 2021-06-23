# a file named "geek", will be opened with the reading mode.
import codecs
file = open('sample.txt', 'r', encoding='utf8')
# This will print no of lines
count = 0
for line in file:
    count += 1
print("Lines = ", count)
# This will print every line one by one in the file
for each in file:
    print(each)
print(file.read())


print(file.read(500))
# Python code to create a file
file = open('samplef.txt', 'w')
file.write("This is the write command\n")
file.write("It allows us to write in a particular file")
# Python code to illustrate with()
with open("sample.txt", encoding='utf8') as file:
	data = file.read()
# do something with data
print(data)
with open("samplef.txt", "w") as f:
    f.write("Hello World!!!")
with open("sample.txt", "r", encoding='utf8') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)
