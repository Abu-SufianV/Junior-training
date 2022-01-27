def lonelyinteger(a):
    dictionary = {}
    for elem in a:
        if elem in dictionary:
            dictionary[elem] += 1
        else:
            dictionary[elem] = 1
    return min(dictionary, key=dictionary.get)


print(lonelyinteger([4, 9, 95, 93, 57, 4, 57, 93, 9]))
