import json
import numpy as np

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

def best_guess(C, Matrix_Offset, lookup, N):
    L = len(C)
    
    # Advanced indexing extracts the columns, and ravel() flattens it instantly 
    # without doing any math operations on the massive array.
    flat_counts = np.bincount(Matrix_Offset[:, C].ravel(), minlength=N * 243)
    counts = flat_counts.reshape(N, 243)
    
    # Direct array mapping instead of float math
    entropies = np.log2(L) - lookup[counts].sum(axis=1) / L
    
    return np.argmax(entropies)
