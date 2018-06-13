s = 'azcbobobegghakl'
numBobs = 0
for x in range(len(s)):
    if s[x:x+3] == "bob":
        numBobs += 1
print("Number of times bob occurs is: " + (str)(numBobs))
