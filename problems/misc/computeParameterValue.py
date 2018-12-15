def computeParameterValue(sources):
    hashmap = {}

    for s in sources:
        print(s)
        for elem in s:
            spl = elem.split(':')
            hashmap[spl[0]] = spl[1]

    return list(hashmap.values())
