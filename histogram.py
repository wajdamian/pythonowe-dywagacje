def histogram(zwrot):
    d = dict()
    for x in zwrot:
        if x in d:
            d[x] = d[x]+1
        else:
            d[x] = 1
    print(d)
