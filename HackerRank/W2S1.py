def sockMerchant(n, ar):
    dictionary = {}
    for elem in ar:
        if elem in dictionary:
            dictionary[elem] += 1
        else:
            dictionary[elem] = 1

    result = 0
    for value in dictionary.values():
        result += value // 2
    return result


print(sockMerchant(1, [1, 2, 1, 2, 1, 3, 2]))
