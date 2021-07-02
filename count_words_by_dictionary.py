counts = dict()
file = open('C://Users//bbiadmin//Documents//Jagannath.txt', "r", encoding='utf8')
data = file.readlines()
for line in data:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
for x in counts:
    print(x + ": " + str(counts[x]))

maxWordCount = 0
maxWord = None
for i, j in counts.items():
    if maxWordCount == 0 or j > maxWordCount:
        maxWord = i
        maxWordCount = j
print("Max word = "+maxWord+"\ncount = "+str(maxWordCount))