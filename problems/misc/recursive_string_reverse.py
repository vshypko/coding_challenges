def reverse_string(s):
    if not s:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("abcdefgh"))