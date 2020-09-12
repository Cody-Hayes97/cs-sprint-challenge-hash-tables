def has_negatives(a):
    # make a dict
    dict = {}
    # make an array of negative number
    res = []
    for i in range(len(a)):
        dict[a[i]] = a[i]
        if a[i] != 0 and - a[i] in dict:
            res.append(abs(a[i]))

    # make an array of positive nums

    return res


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
