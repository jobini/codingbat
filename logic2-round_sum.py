def round10(num):
    last_digit = num % 10
    if last_digit >= 5:
        return num + (10 - last_digit)
    else:
        return num - last_digit

def round_sum(a,b,c):
    a = round10(a)
    b = round10(b)
    c = round10(c)

    return a + b + c
