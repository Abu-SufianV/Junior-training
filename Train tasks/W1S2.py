def miniMaxSum(arr: list[int]) -> str:
    arr = sorted(arr)
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(f"{min_sum} {max_sum}")
