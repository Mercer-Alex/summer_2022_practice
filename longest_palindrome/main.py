def longest_pal(s):
    pal_set = set()

    for char in s:
        if char in pal_set:
            pal_set.remove(char)
        else:
            pal_set.add(char)

    return len(s) - len(pal_set) + 1 if len(pal_set) > 0 else len(s)


pal_string = "abccccdd"

print(longest_pal(pal_string))

