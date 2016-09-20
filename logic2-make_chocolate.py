def make_chocolate(small,big,goal):
    required_big = goal/5
    if big <= required_big:
        required_small = goal - 5 * big
    else:
        required_small = goal - 5 * required_big
    if required_small <= small:
      return required_small
    else:
      return -1
