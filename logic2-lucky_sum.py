def lucky_sum(a,b,c):
    arr = [a,b,c]
    sum = 0
    for i in arr:
        if i == 13:
            return sum
        else:
            sum += i
    return sum
