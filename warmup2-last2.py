def last2(str):
    if str == "":
        return 0
    else:
        last2char = str[-2:]
        count = 0
        for i in range(0,len(str)):
            if str.find(last2char,i,i+2) != -1:
                count += 1
        return count - 1
