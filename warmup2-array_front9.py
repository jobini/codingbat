def array_front9(arr):
    count = 0
    for i in arr:
        if i == 9:
            return True
        else:
            count += 1
            if count == 4:
                return False
    return False
