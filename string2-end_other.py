def end_other(a,b):
    a = a.lower()
    b = b.lower()

    if a in b[-len(a):] or b in a[-len(b):]:
        return True
    else:
        return False
