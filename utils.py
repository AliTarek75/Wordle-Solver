values = {
    "r": 0,
    "y": 1,
    "g": 2
}

def pattern_str_to_code(pattern):
    code = 0
    for i, letter in enumerate(pattern):
        code += (3**i) * values[letter]
    
    return code

def pattern_code_to_str(code):
    str_list = []
    chrs = list(values.keys())

    while (code > 0):
        str_list.append(chrs[int(code % 3)])
        code //= 3
        print(code)

    while (len(str_list) < 5):
        str_list.append("r")

    return ''.join(str_list)