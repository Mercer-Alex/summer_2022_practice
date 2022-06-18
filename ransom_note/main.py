def canConstruct(ransomNote, magazine):
    magDict = {}

    for char in magazine:
        magDict[char] = magDict.get(char, 0) + 1
    for char in ransomNote:
        if char in magDict and magDict[char] > 0:
            magDict[char] = magDict.get(char, 0) - 1
        else:
            return False
    return True

note = "aa"
mag = "ab"

print(canConstruct(note, mag))
