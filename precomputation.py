from utils import *
import json
import numpy as np

def pattern_code(guess, target):
    target_list = list(target)
    guess_list = list(guess)
    pattern = ['r', 'r', 'r', 'r', 'r']

    for i in range(5):
        if target_list[i] == guess_list[i]:
            pattern[i] = 'g'
            guess_list[i] = '_'
            target_list[i] = '_'

    for i in range(5):
        if guess_list[i] != '_':
            for j in range(5):
                if guess_list[i] == target_list[j]:
                    pattern[i] = 'y'
                    target_list[j] = '_'
                    break
    
    return pattern_str_to_code(''.join(pattern))

if __name__ == "__main__":

    with open('words_json/dictionary_5_letter.json', 'r') as f:
        guesses = json.load(f)  # Size G
        
    with open('words_json/targets_5_letter.json', 'r') as f:
        targets = json.load(f)  # Size A

    G = len(guesses)
    A = len(targets)

    Matrix = np.zeros((G, A), dtype=np.uint8)

    print("Building matrix...")
    for i in range(G):
        for j in range(A):
            Matrix[i, j] = pattern_code(guesses[i], targets[j])

    np.save('matrix.npy', Matrix)

    print("Done!")