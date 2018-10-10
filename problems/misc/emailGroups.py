def solution(L):
    emailGroups = {}

    for email in L:
        splitString = email.split("@")
        domain = splitString[-1]

        local = splitString[0:len(splitString)-1]
        local = str(local).replace(".", "")[2:-2]
        local = local.split("+")[0]

        formattedEmail = local + "@" + domain

        if formattedEmail not in emailGroups.keys():
            emailGroups[formattedEmail] = 1
        else:
            emailGroups[formattedEmail] += 1

    return sum(1 for counter in emailGroups.values() if counter > 1)


L = ["a.b@example.com", "x@example.com", "‹x@exa.mple.com",
     "ab+1@example.com", "y@example.com", "y@example.com", "y@example.com", "z.......@example.com"]
print(solution(L))
