def maxFlorists(pathLength, floristIntervals):
    counter = 0
    lengthMap = {}
    floristIntervals = sorted(floristIntervals, key=lambda i: i[0])
    print(floristIntervals)

    for i in range(pathLength):
        lengthMap[i] = 0

    for interval in floristIntervals:
        if interval[0] >= pathLength:
            continue

        canPlant = False

        index = interval[0]
        upTo = interval[1]

        i = index
        while i < upTo:
            if (i in lengthMap.keys()) and (lengthMap[i] < 3):
                canPlant = True
            else:
                canPlant = False
                break
            i += 1

        if canPlant:
            i = index
            while i < upTo:
                lengthMap[i] += 1
                i += 1
            counter += 1

    return counter
