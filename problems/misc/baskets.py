def solution(A):
    passMaxValue, firstBasket, secondBasket = {}, {}, {}
    first, second, numPass = 0, 0, 0

    for fruitType in A:
        if fruitType not in firstBasket.keys() and fruitType not in secondBasket.keys():
            if len(firstBasket.keys()) == 0 and len(secondBasket.keys()) == 0:
                firstBasket[fruitType] = 1
            elif len(firstBasket.keys()) == 1 and len(secondBasket.keys()) == 0:
                secondBasket[fruitType] = 1
            elif len(firstBasket.keys()) == 1 and len(secondBasket.keys()) == 1:
                first = firstBasket[list(firstBasket)[0]]
                second = secondBasket[list(secondBasket)[0]]
                passMaxValue[numPass] = first + second
                first, second = 0, 0

                numPass += 1
                firstBasket, secondBasket = {}, {}
                firstBasket[fruitType] = 1
            continue
        elif fruitType in firstBasket.keys():
            firstBasket[fruitType] += 1
            continue
        elif fruitType in secondBasket.keys():
            secondBasket[fruitType] += 1
            continue

    for fruitType in A[1:]:
        if fruitType not in firstBasket.keys() and fruitType not in secondBasket.keys():
            if len(firstBasket.keys()) == 0 and len(secondBasket.keys()) == 0:
                firstBasket[fruitType] = 1
            elif len(firstBasket.keys()) == 1 and len(secondBasket.keys()) == 0:
                secondBasket[fruitType] = 1
            elif len(firstBasket.keys()) == 1 and len(secondBasket.keys()) == 1:
                first = firstBasket[list(firstBasket)[0]]
                second = secondBasket[list(secondBasket)[0]]
                passMaxValue[numPass] = first + second
                first, second = 0, 0

                numPass += 1
                firstBasket, secondBasket = {}, {}
                firstBasket[fruitType] = 1
            continue
        elif fruitType in firstBasket.keys():
            firstBasket[fruitType] += 1
            continue
        elif fruitType in secondBasket.keys():
            secondBasket[fruitType] += 1
            continue

    numPass += 1
    if firstBasket:
        first = firstBasket[list(firstBasket)[0]]
    if secondBasket:
        second = secondBasket[list(secondBasket)[0]]
    passMaxValue[numPass] = first + second

    return max(passMaxValue.values())


A = [1, 2, 3, 1]
print(solution(A))
