def get_indices_of_item_weights(weights, length, limit):
    # cache = {}

    # for i in range(len(weights)):
    #     cache[weights[i]] = i

    # for i in range(len(weights)):
    #     l_w = limit - weights[i]

    #     if l_w in cache:
    #         return (max(i, cache[l_w]), min(i, cache[l_w]))
    # # return 2 items added together to make limit
    # # make a dict
    dict = {}
    for idx, weight in enumerate(weights):
        dict[weight] = idx

    for idx, weight in enumerate(weights):
        value = limit - weight

        if value in dict:
            return (max(idx, dict[value]), min(idx, dict[value]))

    # # for i in range(len(weights)):
    # #     for j in range(i + 1):
    # #         if weights[i] + weights[j] == limit:
    # #             return (i, j)
    # return None
    # # return idexes of items, not items themselves
    # # return the 2 idexes as a tuple
    # # if nothing adds up to limit, return none


print(get_indices_of_item_weights(
    weights=[4, 6, 10, 15, 16], length=5, limit=21))
