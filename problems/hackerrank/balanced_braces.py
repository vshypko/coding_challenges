def braces(values):
    opening_braces = ['(', '[', '{']
    result_list = list()

    for value in values:
        stack = []
        is_balanced = True
        for brace in value:
            if brace in opening_braces:
                stack.append(brace)
            else:
                if not stack or not is_balanced_pair(stack.pop(), brace):
                    is_balanced = False
                    break
        if len(stack) == 0 and is_balanced:
            result_list.append("YES")
        else:
            result_list.append("NO")

    return result_list


def is_balanced_pair(opening, closing):
    return (opening == '(' and closing == ')') \
           or (opening == '[' and closing == ']') \
           or (opening == '{' and closing == '}')
