s = "awemodxil"
numVowels = 0
for a in range(len(s)):
    l = s[a]
    if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
        numVowels += 1
print("Number of vowels: " + (str)(numVowels))
