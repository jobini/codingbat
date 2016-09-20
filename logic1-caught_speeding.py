def caught_speeding(speed, is_birthday):
    s_limit = 60
    b_limit = 80

    if is_birthday:
        s_limit += 5
        b_limit += 5

    if speed <= s_limit:
        return 0
    elif speed > s_limit and speed <= b_limit:
        return 1
    else:
        return 2
