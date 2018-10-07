def multTable(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i*j, end="\t", flush=True)
        print()


print(multTable(12))
