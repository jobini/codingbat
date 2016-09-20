def fix_teen(n):
    if n in range(13,20):
        if n == 15 or n == 16:
            return n
        else:
            return 0
    else:
        return n

def no_teen_sum(a,b,c):
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)

    return a + b + c
