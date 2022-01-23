def timeConversion(s: str) -> str:
    line = s.split(":")
    midday = line[-1][-2:]
    line[-1] = line[-1][:2]

    if midday == "AM" and line[0] == "12":
        line[0] = "00"
    elif midday == "PM" and line[0] != "12":
        line[0] = str(int(line[0]) + 12)

    time = ":".join(line)
    return time


print(timeConversion("12:45:54PM"))
