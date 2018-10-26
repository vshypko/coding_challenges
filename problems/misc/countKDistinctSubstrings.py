def countKDistinctSubstrings(inputString, num):
    resultCounter = 0
    lengthOfString = len(inputString)

    for i in range(lengthOfString):
        distanceCounter = 0
        countArray = [0] * 26  # store alphabet character counter by its id
        for j in range(i, lengthOfString):
            if countArray[ord(inputString[j]) - ord('a')] == 0:
                distanceCounter += 1

            countArray[ord(inputString[j]) - ord('a')] += 1

            if distanceCounter == num:
                resultCounter += 1
    return resultCounter
