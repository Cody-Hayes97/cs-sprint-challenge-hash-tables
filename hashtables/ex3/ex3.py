def intersection(arrays):
    # make dict
    dict = {}
    # loop through 2d array
    res = []

    for row in arrays:
        for column in row:
            if column not in dict:
                dict[column] = 1
            else:
                dict[column] += 1
                if dict[column] == len(arrays):
                    res.append(column)
    return res


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
