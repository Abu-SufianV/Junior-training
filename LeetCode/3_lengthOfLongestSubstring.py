def lengthOfLongestSubstring(s: str) -> int:
    s = list(s)
    best = []
    cur = []
    i = 0
    while i < len(s):
        if s[i] not in cur:
            cur.append(s[i])
            i += 1
        else:
            best = best if len(best) > len(cur) else cur
            cur = []
    return max(len(best), len(cur))


print(lengthOfLongestSubstring(" "))
