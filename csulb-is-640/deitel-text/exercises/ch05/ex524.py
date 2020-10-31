'''
5.24 (Card Shuffling and Dealing) In Exercises 5.24 through 5.26, you’ll use lists of 
tuples in scripts that simulate card shuffling and dealing. Each tuple represents one card in
the deck and contains a face (e.g., 'Ace', 'Deuce', 'Three', …, 'Jack', 'Queen', 'King')
and a suit (e.g., 'Hearts', 'Diamonds', 'Clubs', 'Spades'). Create an initialize_deck
function to initialize the deck of card tuples with 'Ace' through 'King' of each suit, as in

    deck = [('Ace', 'Hearts'), …, ('King', 'Hearts'),
    ('Ace', 'Diamonds'), …, ('King', 'Diamonds'),
    ('Ace', 'Clubs'), …, ('King', 'Clubs'),
    ('Ace', 'Spades'), …, ('King', 'Spades')]

Before returning the list, use the random module’s shuffle function to randomly order the
list elements. Output the shuffled cards in the following four-column format:
    Six of Spades       Eight of Spades     Six of Clubs        Nine of Hearts
    Queen of Hearts     Seven of Clubs      Nine of Spades      King of Hearts
    Three of Diamonds   Deuce of Clubs      Ace of Hearts       Ten of Spades
    Four of Spades      Ace of Clubs        Seven of Diamonds   Four of Hearts
    Three of Clubs      Deuce of Hearts     Five of Spades      Jack of Diamonds
    King of Clubs       Ten of Hearts       Three of Hearts     Six of Diamonds
    Queen of Clubs      Eight of Diamonds   Deuce of Diamonds   Ten of Diamonds
    Three of Spades     King of Diamonds    Nine of Clubs       Six of Hearts
    Ace of Spades       Four of Diamonds    Seven of Hearts     Eight of Clubs
    Deuce of Spades     Eight of Hearts     Five of Hearts      Queen of Spades
    Jack of Hearts      Seven of Spades     Four of Clubs       Nine of Diamonds
    Ace of Diamonds     Queen of Diamonds   Five of Clubs       King of Spades
    Five of Diamonds    Ten of Clubs        Jack of Spades      Jack of Clubs
'''
def card_str(card=('','')):
    return f'{card[0]} of {card[1]}'

def list_to_multidim(list_to_multidim = [], column_count = 1):
    in_list = list_to_multidim
    col = 1
    if column_count >= 1:
        col = column_count

    out_list = []
    row = []
    for count, item in enumerate(in_list, 1):
        row.append(item)
        if count % col == 0:
            out_list.append(row)
            row = []
    
    return out_list
    
def print_deck(deck=[]):
    in_deck = deck
    in_deck = [card_str(c) for c in in_deck]
    in_deck = list_to_multidim(in_deck, 4)
    for row in in_deck:
        for card in row:
            print(f'{card:<20}', end='')
        print()

def initialize_deck(verbose=False):
    import random
    deck = []
    faces = ('Ace', 'Deuce', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    deck = [(face, suit) for face in faces for suit in suits]
    
    random.shuffle(deck)

    if verbose:
        print_deck(deck)

    return deck

deck = initialize_deck(verbose=True)

pass