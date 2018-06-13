s = 'ddlrfnqkqfcjqcfuwtgrbvhz'
print(len(s))
longestLength = -1
longestSubstring = ''
for n in range(len(s)):
    currLength = 1
    currSubstring = s[n]
    currCount = n
    currLetter = s[currCount]
    if currCount != len(s) - 1:
        nextLetter = s[currCount + 1]
    while currLetter <= nextLetter and currCount != len(s) - 1:
        currSubstring += nextLetter
        currLength += 1
        currCount += 1
        if currCount != len(s) - 1:
            currLetter = s[currCount]
            nextLetter = s[currCount + 1]
    if currLength > longestLength:
        longestLength = currLength
        longestSubstring = currSubstring
print("Longest substring in alphabetical order is: " + longestSubstring)
