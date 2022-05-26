a = "abc"
b = "acb"

c = "abcde"
d = "cdeab"

e = "a"
f = "b"


def same(first, second):
    for x in range(len(first)):
        print(x)
        if first == second:
            return True
        else:
            first = first[1:] + first[0]
    return False

print(same(a, b))

print(same(c, d))

print(same(e, f))