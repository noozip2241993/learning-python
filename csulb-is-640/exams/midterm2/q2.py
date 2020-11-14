def main():
    START = ord('A')
    END = ord('Z')
    COUNT = 30

    import random
    #rando_letters = []
    #for x in range(COUNT):
    #    rando_letters.append(chr(random.randint(START, END)))

    rando_letters = [chr(random.randint(START, END)) for _ in range(COUNT)]

    print(sorted(rando_letters, reverse=False))
    unique = list(set(rando_letters))
    print(sorted(unique, reverse=True))

main()