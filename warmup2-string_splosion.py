def string_splosion(str):
    newstr = str[0]
    for i in range(2,len(str)+1):
        newstr = newstr + str[0:i]
    return newstr
