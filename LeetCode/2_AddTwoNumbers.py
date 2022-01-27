def addTwoNumbers(l1: list[int], l2: list[int]) -> list[int]:
    num_1 = int("".join(reversed(list(map(str, l1)))))
    num_2 = int("".join(reversed(list(map(str, l2)))))
    result = list(reversed(list((map(int, str(num_1 + num_2))))))
    return result


print(addTwoNumbers([2, 4, 3], [5, 6, 4]))
