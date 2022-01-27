def two_sum(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]


assert two_sum([1, 2, 3, 4, 5], 5) == [0, 3]
