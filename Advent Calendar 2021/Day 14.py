with open('Day_14_Input.txt', "r") as f:
    myinput = (f.read().splitlines())

key = dict()

words = myinput[:myinput.index('')]
#words = list(words[0])
words = (words[0])
keys = myinput[myinput.index('')+1:]

for i in range(len(keys)):
    key[keys[i][:2]] = keys[i][(len(keys[i]))-1:]

for k in range(10):
    print(k)
    p = 0
    for i in range(len(words)):
        i += p
        #word = ''.join(words[i:i+2])
        word = words[i:i+2]
        if len(word) >= 2:
            if word in key:
                p += 1
                #words.insert(i+1,key[word])
                words = words[:i+1] + key[word] + words[i+1:]

counts = dict()
for i in words:
  counts[i] = counts.get(i, 0) + 1

print(len(words))

print(counts[(max(counts, key=counts.get))]-counts[min(counts, key=counts.get)])