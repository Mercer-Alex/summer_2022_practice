def valid(string):
    stack = []

    if len(string) <= 1:
        return False

    for x in string:
        if x == "(" or x == "[" or x == "{":
            stack.append(x)
        elif x == ")" and len(stack) >= 1 and stack[-1] == "(":
            stack.pop()
        elif x == "]" and len(stack) >= 1 and stack[-1] == "[":
            stack.pop()
        elif x == "}" and stack[-1] == "{":
            stack.pop()
        else:
            return False
    if len(stack) > 0:
        return False
    else:
        return True

str1 = "(){}"

str2 = "()["

print(valid(str1))

print(valid(str2))

