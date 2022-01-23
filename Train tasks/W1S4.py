def matchingStrings(strings: list[str], queries: list[str]) -> list[int]:
    result = []
    for line in queries:
        result.append(strings.count(line))
    return result


print(matchingStrings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc']))
