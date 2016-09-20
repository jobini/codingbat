def front_back(str):
    if len(str) >= 2:
        first = str[0]
        middle = str[1:-1]
        last = str[-1]
        return last + middle + first
    else:
        return str
