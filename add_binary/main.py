def addBinary(a, b):
    result = ""

    carry = 0
    a = list(a)
    b = list(b)

    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())

        result = str(carry % 2) + result
        carry //= 2
    return result


bina = "1010"
binb = "1011"

print(addBinary(bina, binb))
