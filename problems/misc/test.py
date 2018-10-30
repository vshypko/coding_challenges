class Solution:
    def __init__(self):
        # for testing purposes
        pass

    def findSchedules(self, workHours, dayHours, pattern):
        hoursToGo = workHours
        numOfDays = 0
        indexToAdd = list()
        resultList = list()

        for i in range(len(pattern)):
            if pattern[i] == '?':
                indexToAdd.append(i)
                numOfDays += 1
            else:
                hoursToGo -= int(pattern[i])

        permutations = self.generatePermutations(numOfDays, hoursToGo, dayHours)

        for permutation in permutations:
            if sum(permutation) != hoursToGo or len(permutation) != numOfDays:
                continue
            index = 0
            listString = list(pattern)
            for i in indexToAdd:
                listString[i] = permutation[index]
                index += 1
            stringToAdd = ''.join(str(x) for x in listString)
            resultList.append(stringToAdd)
        return resultList

    # TODO: max number in permutation == dayHours
    def generatePermutations(self, numberOfDays, sumUpTo, dayHours):
        if numberOfDays < 0 or sumUpTo < 0:
            return
        elif numberOfDays == 0:
            return []
        elif numberOfDays == 1:
            return [[dayHours]]
        elif sumUpTo == 0:
            return [[0] * numberOfDays]
        decreaseNumberOfDays = [[0] + hours for hours in self.generatePermutations(numberOfDays - 1, sumUpTo, dayHours)]
        decreaseSumUpTo = [[hours[0] + 1] + hours[1:] for hours in self.generatePermutations(numberOfDays, sumUpTo - 1, dayHours)]

        return decreaseNumberOfDays + decreaseSumUpTo


# print(Solution().findSchedules(56, 8, "???8???"))
