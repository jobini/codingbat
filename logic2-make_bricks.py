def make_bricks(small,big,goal):
    required_big = goal/5
    if big <= required_big:
        required_small = goal - 5 * big
    else:
        required_small = goal - 5 * required_big
    if small < required_small:
        return False
    else:
        return True
