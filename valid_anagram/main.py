
def valid_anagram(string1, string2):
    dict1 = {}
    dict2 = {}

    for x in string1:
        dict1[x] = dict1.get(x, 0) + 1
    for x in string2:
        dict2[x] = dict2.get(x, 0) + 1

    return dict1 == dict2

word = "bob"

ana = "obb"

print(valid_anagram(word, ana))
