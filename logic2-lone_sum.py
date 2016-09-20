def lone_sum(a,b,c):
    arr = [a,b,c]
    b = []
    sum = 0
    for i in arr:
        if i not in b:
            b.append(i)
    for i in arr:
        c = arr.count(i)
        if c > 1:
            try:
                b.remove(i)
            except:
                continue
    for i in b:
        sum = sum + i
    return sum
