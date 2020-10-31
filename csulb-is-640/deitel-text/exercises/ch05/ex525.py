'''
5.25 (Card Playing: Evaluating Poker Hands) Modify Exercise 5.24 to deal a five-card
poker hand as a list of five card tuples. Then create functions (i.e., is_pair, is_two_pair,
is_three_of_a_kind, …) that determine whether the hand they receive as an argument
contains groups of cards, such as:
    a) one pair
    b) two pairs
    c) three of a kind (e.g., three jacks)
    d) a straight (i.e., five cards of consecutive face values)
    e) a flush (i.e., all five cards of the same suit)
    f) a full house (i.e., two cards of one face value and three cards of another)
    g) four of a kind (e.g., four aces)
    h) straight flush (i.e., a straight with all five cards of the same suit)
    i) … and others.
See https://en.wikipedia.org/wiki/List_of_poker_hands for poker-hand types and
how they rank with respect to one another. For example, three of a kind beats two pairs.
'''

FACES = ('Ace', 'Deuce', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
HANDS = ('Straight Flush', 'Four of a Kind', 'Full House', 'Flush', 'Straight', 'Three of a Kind', 'Two Pair', 'One Pair', 'High Card')

def card_str(card=('','')):
    return f'{card[0]} of {card[1]}'

def list_to_multidim(list_to_multidim=[], column_count=1):
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

def print_cards(cards=[]):
    in_cards = cards
    [print(card_str(card)) for card in in_cards]

def initialize_deck(faces=FACES, suits=SUITS, verbose=False):
    import random
    deck = []
    in_faces = faces
    in_suits = suits

    deck = [(face, suit) for face in in_faces for suit in in_suits] #build the deck
    random.shuffle(deck) #shuffle the deck
    if verbose:
        print_deck(deck) #if called for in the args, print the deck

    return deck

def deal_hand(deck=initialize_deck(FACES, SUITS), cards_in_hand=5):
    hand = [deck.pop(0) for x in range(cards_in_hand)]
    print_cards(hand)
    return hand

def read_poker_hand(hand, verbose=False):
    in_hand = hand
    # count the frequency of faces and suits in the hand
    face_freq = tuple([(f, len([c[0] for c in in_hand if c[0] == f])) for f in FACES])
    suit_freq = tuple([(s, len([c[1] for c in in_hand if c[1] == s])) for s in SUITS])

    # count the frequency of different poker hands
    poker_hand = HANDS[-1]
    pair_count = len(list(filter(lambda face: face[1] == 2, face_freq)))
    if pair_count == 1:
        poker_hand = HANDS[-2]
    elif pair_count == 2:
        poker_hand = HANDS[-3]

    triple_count = len(list(filter(lambda face: face[1] == 3, face_freq)))
    if triple_count:
        poker_hand = HANDS[-4]

    straight_count = 0
    if straight_count:
        poker_hand = HANDS[-5]

    flush_count = len(list(filter(lambda suit: suit[1] == 5, suit_freq)))
    if flush_count:
        poker_hand = HANDS[-6]

    full_house_count = 0
    if (pair_count == 1 and triple_count == 1):
        full_house_count = 1
        pair_count = 0
        triple_count = 0
        poker_hand = HANDS[-7]
        
    four_count = len(list(filter(lambda face: face[1] == 4, face_freq)))
    if four_count:
        poker_hand = HANDS[-8]

    straight_flush_count = 0
    if (straight_count == 1 and flush_count == 1):
        straight_flush_count = 1
        straight_count = 0
        flush_count = 0
        poker_hand = HANDS[-9]

    if verbose:
        print(f'{"Pairs:":>18} {pair_count:>}')
        print(f'{"Three of a Kind:":>18} {triple_count:>}')
        print(f'{"Straight:":>18} {straight_count:>}')
        print(f'{"Flush:":>18} {flush_count:>}')
        print(f'{"Full House:":>18} {full_house_count:>}')
        print(f'{"Four of a Kind:":>18} {four_count:>}')
        print(f'{"Straight Flush:":>18} {straight_flush_count:>}')
    
    hand_rank = HANDS.index(poker_hand)
    print(poker_hand)
    return hand_rank

def play_poker():
    deck = initialize_deck()

    print('hand_a')
    print('-------------------')
    hand_a = deal_hand(deck)
    print('-------------------')
    hand_a_rank = read_poker_hand(hand_a)

    print()

    print('hand_b')
    print('-------------------')
    hand_b = deal_hand(deck)
    print('-------------------')
    hand_b_rank = read_poker_hand(hand_b)

    print()

    if hand_a_rank < hand_b_rank:
        print('hand_a wins')
    elif hand_b_rank < hand_a_rank:
        print('hand_b wins')
    else:
        print('tie')

play_poker()
