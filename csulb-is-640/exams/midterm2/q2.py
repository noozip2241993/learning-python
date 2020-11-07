def main():
    START = ord('A')
    END = ord('Z')
    COUNT = 30

    import random
    rando_letters = []
    for i in range(COUNT):
        letter = chr(random.randint(START, END))
        rando_letters.append(letter)

    print(sorted(rando_letters, reverse=False))
    print(sorted(rando_letters, reverse=True))

main()