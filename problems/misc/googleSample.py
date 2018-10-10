# License key. Insert "-" every K characters except possibly the first group.
def solution(S, K):
    if len(S) <= K:
        return S

    listS = list(S.replace("-", ""))
    print(listS)

    i = len(listS)
    while i > K:
        i -= K
        listS.insert(i, "-")

    result = "".join(listS)
    print(result)


solution("2-4A0r7-4k", 4)
