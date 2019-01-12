# 8.4

# O(2^n) runtime
# O(2^n) space
def powerSet(s, index=0):
    if len(s) == index:
        allSubsets = list()
        allSubsets.append(list())
    else:
        allSubsets = powerSet(s, index + 1)
        item = s[index]
        moreSubsets = list()

        for subset in allSubsets:
            newSubset = list(subset)
            newSubset.append(item)
            moreSubsets.append(newSubset)
        allSubsets.extend(moreSubsets)

    return allSubsets


print(powerSet([]))
print(powerSet([1]))
print(powerSet([1, 2]))
print(powerSet([1, 2, 3]))
print(powerSet([1, 2, 3, 4]))
print(powerSet([1, 2, 3, 4, 5]))
