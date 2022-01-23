def plusMinus(arr: list[int]) -> None:
    amount_values = [0 for i in range(3)]
    for i in arr:
        if i > 0:
            amount_values[0] += 1
        elif i < 0:
            amount_values[1] += 1
        else:
            amount_values[2] += 1

    print(round(amount_values[0] / len(arr), 6))
    print(round(amount_values[1] / len(arr), 6))
    print(round(amount_values[2] / len(arr), 6))