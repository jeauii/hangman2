import sys
import numpy as np

WORD_LEN = 16

def generate_input(cipher):
    input = np.zeros((WORD_LEN, 27))
    cipher = cipher[:WORD_LEN]
    for i, ch in enumerate(cipher):
        if ch.isalpha():
            input[i][ord(ch) - 97] = 1
        elif ch == '.':
            input[i][26] = 1
        else:
            assert False, f"invalid character {ch}"
    return input

def generate_output(key):
    output = np.zeros(26)
    for ch in key:
        if ch.isalpha():
            output[ord(ch) - 97] += 1
        else:
            assert False, f"invalid character {ch}"
    output /= len(key)
    return output

def main():
    x_train, y_train = [], []
    for line in sys.stdin:
        split = line.split(None, 2)
        x_train.append(generate_input(split[0]))
        y_train.append(generate_output(split[1]))

    np.savez_compressed(sys.argv[1], x=x_train, y=y_train)

if __name__ == '__main__':
    main()
