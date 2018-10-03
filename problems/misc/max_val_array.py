def max_num_array(A):
    max = float('-inf')
    for item in A:
        if item > max:
            max = item
    return max

print(max_num_array([1,5,212,63,5231,355,-7753]))
