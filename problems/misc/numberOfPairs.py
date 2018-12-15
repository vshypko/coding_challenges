def numberOfPairs(a, k):
    counter = 0
    pairs = set()
    a.sort()

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == k and (a[i], a[j]) not in pairs:
                counter += 1
                pairs.add((a[i], a[j]))

    return counter
