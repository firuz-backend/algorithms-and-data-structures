def polynomial_sum(tup1, tup2):
    len1 = len(tup1)
    len2 = len(tup2)
    tup1 = list(tup1)
    tup2 = list(tup2)
    res = list()

    if len1 < len2:
        extend = [0] * (len2 - len1)
        tup1 = extend + tup1
    if len2 < len1:
        extend = [0] * (len1 - len2)
        tup2 = extend + tup2

    for i in range(len(tup1)):
        res.append(tup1[i] + tup2[i])

    i = 0
    while True:
        if res[i] == 0:
            res.pop(i)
            if res[i] != 0:
                break
        else:
            break
        i += 1

    return tuple(res)


print(polynomial_sum((2, -4, 5), (3, 2)))
print(polynomial_sum((1, 7, 0, -4), (-1, 0, 0, 2)))
print(polynomial_sum((1, 2, 3, 4, 5), (1,)))
