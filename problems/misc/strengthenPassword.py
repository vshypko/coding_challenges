def strengthenPasswords(passwords):
    i = 0
    for password in passwords:
        current = password
        current = current.replace('s', '5').replace('S', '5')

        if (len(current) != 1 and len(current) % 2 == 1
                and current[len(current) // 2].isdigit()):
            current = list(current)
            current[len(current) // 2] = str(int(current[len(current) // 2]) * 2)
            current = ''.join(current)

        if len(current) % 2 == 0:
            current = list(current)
            current[0], current[len(current) - 1] = (current[len(current) - 1].upper()
                                                     if current[len(current) - 1].islower()
                                                     else current[len(current) - 1].lower(),
                                                     current[0].upper()
                                                     if current[0].islower()
                                                     else current[0].lower())
            current = ''.join(current)

        lowerCurrent = current.lower()
        index = lowerCurrent.find('nextsmth')
        if index != -1:
            temp = current[index:index + len('nextsmth')]
            temp = list(temp)
            temp[0], temp[1], temp[2], temp[3] = temp[3], temp[2], temp[1], temp[0]
            before = current[0:index]
            temp = ''.join(temp)
            after = current[index + len('nextsmth'):]
            current = before + temp + after

        passwords[i] = current
        i += 1

    return passwords
