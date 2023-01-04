import sys, string, random
import numpy as np
import tensorflow as tf
from process import get_word
from generate import generate_input

RANDOM_SEED = 0
HANGMAN_LIVES = 26

def random_word(file):
    with open(file) as vocab:
        for i, line in enumerate(vocab):
            if random.randint(0, i) == 0:
                word = get_word(line)
    return word

def main():
    random.seed(RANDOM_SEED)

    model = tf.keras.models.load_model(sys.argv[1])

    count = (0, 0)
    for line in sys.stdin:
        try:
            word = get_word(line)
        except:
            word = random_word(sys.argv[2])
            
        print(word)
        
        lives = HANGMAN_LIVES
        guesses = ''
        cipher = '.' * len(word)
        while '.' in cipher and lives != 0:
            prob = model(np.asarray([generate_input(cipher)]))[0]
            for i in reversed(np.argsort(prob)):
                letter = chr(i + 97)
                if letter in guesses:
                    continue
                guesses = guesses + letter
                print(f"{cipher} => {letter} ({lives})")
                print(''.join('{:5}'.format(ch) for ch in string.ascii_lowercase))
                print(''.join('{:4.0f}%'.format(p * 100) for p in prob))
                count = (count[0] + 1, count[1] + 1 if letter in word else count[1])
                if letter in word:
                    cipher = ''.join(ch if ch == letter else cipher[i] for i, ch in enumerate(word))
                    break
                else:
                    lives -= 1
                    if lives == 0:
                        break
        print('.' not in cipher)
    print(f'{count[1]}/{count[0]}')

if __name__ == '__main__':
    main()
