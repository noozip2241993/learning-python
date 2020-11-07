def main():
    START = ord('A')
    END = ord('Z')
    COUNT = 30

    import random
    rando_letters = [chr(random.randint(START, END)) for _ in range(COUNT)]

    print(sorted(rando_letters, reverse=False))
    print(sorted(rando_letters, reverse=True))

main()