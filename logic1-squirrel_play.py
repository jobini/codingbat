def squirrel_play(temp,is_summer):
    u_lim = 90
    if is_summer:
        u_lim = 100
    if temp in range(60,u_lim + 1):
        return True
    else:
        return False
