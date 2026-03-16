# Information-Theoretic Wordle Solver

A Python-based Wordle solver that uses Entropy to find the mathematically optimal guess. Instead of relying on heuristic word lists, this solver calculates the expected information gain for every possible word across all remaining valid targets, and then narrows down the search space until only one guess remains in the fewest turns possible.



## Requirements
* **Python 3.x**
* **NumPy**



## Setup
The solver relies on a precomputed pattern matrix (`matrix.npy`) to perform fast calculations.

If `matrix.npy` is not already in the repository, you can generate it locally:
1. Ensure the two dictionary files (`targets_5_letter.json` and `dictionary_5_letter.json`) are located in the `words_json/` directory.
2. Run the precomputation script:

```bash
python precomputation.py
```



## Usage
Run the main solver script:

```bash
python main.py
```

### Inputs
The script will prompt you for two inputs during each round:
* **[?] Guess:** The 5-letter word you inputted into Wordle.
* **[?] Feedback:** A 5-character string representing the colors Wordle returned:
    * `g` = Green (Correct letter, correct spot)
    * `y` = Yellow (Correct letter, wrong spot)
    * `r` = Red/Gray (Letter not in word)

**Example:** If Wordle returns Green-Red-Yellow-Red-Red, you type `gryrr`.


## Outputs & Metrics
* **Current Entropy:** The total uncertainty remaining in the game (in bits). A value of 0 means only one possible word is left.
* **Expected Best-Guess Entropy:** The average amount of uncertainty we expect to eliminate by choosing the top suggested word.
* **Top Suggestions:** The top 10 recommended words, strictly ranked by their expected information gain.


## Example Output
```text
-------------------- Round 1 ---------------------
[i] Remaining answers: 3242
[i] Current entropy: 11.663 bits
[i] Actual Information gained (Surprise): 0 bits
--------------------------------------------------
[+] Processing Guesses...
[+] Finished in: 2.09s

Top suggestions:
    1. soare    Entropy = 5.9783
    2. raise    Entropy = 5.9479
    3. salet    Entropy = 5.927
    ...

[i] Expected Best-Guess Entropy (Information gain): 5.978 bits
[i] Expected posterior entropy using the best-guess: 5.685 bits
```

## Common Errors
* ```[!] Error: '...' is not in the dictionary``` The word you guessed is not recognized by the internal Wordle dictionary.
* ```[!] Error: Pattern must be 5 chars...``` You entered an invalid feedback. It must be exactly 5 characters long using only `r`, `y`, or `g`.
* ```[!] Contradiction Error``` The solver eliminated all possible words. This strictly means a previous feedback string was entered incorrectly, making the current board state mathematically impossible.
