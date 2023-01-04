import sys, random

def get_word(line):
    split = line.split(None, 1)
    assert split[0].isalpha(), 'non-alpha character'
    return split[0].lower()

def process_word(word, index=0, key=""):
    for i, ch in enumerate(word[index:]):
        if ch != '.' and ch not in word[:index + i]:
            cipher = word.replace(ch, '.')
            print(f'{cipher} {key + ch}')
            process_word(cipher, index + i + 1, key + ch * word.count(ch))

def main():
    rate = 1 if len(sys.argv) == 1 else float(sys.argv[1])

    for line in sys.stdin:
        if random.random() < rate:
            process_word(get_word(line))

if __name__ == '__main__':
    main()
