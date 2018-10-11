def reverseString(s):
    if not s:
        return s
    return reverseString(s[1:]) + s[0]


print(reverseString("abcdefgh"))
