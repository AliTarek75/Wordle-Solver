import json
import numpy as np
import time
import sys

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

def row_entropy(row):
    
    _, counts = np.unique(row, return_counts=True)
    probs = counts / len(row)

    entropies = np.log2(probs) * probs
    
    return - np.sum(entropies)

def pattern_is_valid(pattern):
    allowed = {'r', 'g', 'y'}
    return len(pattern) == 5 and all(char in allowed for char in pattern)

def get_input(prompt_text):
    if sys.stdout.isatty():
        return input(prompt_text)
    else:
        return input()

def best_guess(Matrix, C):

    entropies = [row_entropy(np.array(row)) for row in Matrix[:, C]]

    best_guesses = np.argsort(entropies)[::-1][:10]
    best_entropies = np.sort(entropies)[::-1][10:]

    return [best_guesses, best_entropies]

