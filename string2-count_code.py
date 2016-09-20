def d_converter(str):
    i_array = []
    list_str = list(str)
    final_str = ""
    for i in range(0, len(str) - 3):
        if str[i:i+2] == "co":
            i_array.append(i+2)
    for i in i_array:
        list_str[i] = "d"
    return final_str.join(list_str)

def count_code(str):
    str = d_converter(str)
    return str.count("code")
