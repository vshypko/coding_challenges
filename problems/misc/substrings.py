def substrings(string, k):
    result = list()
    strs = set()

    for i in range(len(string) - k + 1):
        substr = string[i:i+k]
        if substr not in strs:
            strs.add(substr)

    for s in strs:
        result.append(s)
    return result


result = substrings("abcd", 2)
assert 'ab' in result
assert 'bc' in result
assert 'cd' in result
