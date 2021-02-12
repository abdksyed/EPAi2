import random

vals = ['2', '3', '4', '5', '6', '7', '8',
        '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
internal_vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

deck_lam = list(map(lambda x: (x[0], x[1]), zip(vals*4, suits*13)))


def create_deck(vals: list,
                suits: list,
                number_of_decks: int = 1) -> set:
    '''
    A function which creates a deck of playing cards.
    Arguments:
    vReturn: The values of cards of each suit.
    suits: The diffrent suits of cards.
    number_of_decks: Number of decks to be used.
    Returns:
    deck: Set of Cards.
    '''
    if not isinstance(vals, (list, set, tuple)):
        raise TypeError('vals must be a iterable')
    if not isinstance(suits, (list, set, tuple)):
        raise TypeError('suits must be a iterable')
    if not isinstance(number_of_decks, int):
        raise TypeError('number_of_decks must be of type <int>')
    if number_of_decks <= 0:
        raise ValueError('Number of Decks must be a positive number.')

    deck = set()
    for _ in range(number_of_decks):
        for suit in suits:
            for val in vals:
                deck.add((val, suit))
    return deck


def conv_card_to_num(card: str) -> int:
    '''
    Convert the Card to an integer value.
    Argument: card of str type
    Returns: The integer value of the card.
    '''
    if card == 'ace':
        return 14
    if card == 'king':
        return 13
    if card == 'queen':
        return 12
    if card == 'jack':
        return 11
    return int(card)


def royal_flush(hand: list) -> tuple:
    '''
    Check if hand is a Royal Flush.
    Argument: The set of card - hand
    Return:
    If True, Return (Rank:1, string), (14)
    If False, Return False, None
    '''
    val = [x[0] for x in hand]
    suit = [x[1] for x in hand]
    royal_flush = ['ace', 'king', 'queen', 'jack', '10']
    if len(set(suit)) != 1:
        return False, None
    k = 0
    for i in range(len(hand)):
        if val[i] in royal_flush[:len(hand)]:
            k += 1
    if k == len(hand):
        return (1, 'WOW!!!!. You got a "ROYALLLLLLL FLUSH!"(Rank:1)'), (14,)
    return False, None


def straight_flush(hand: list) -> tuple:
    '''
    Check if hand is a Straight Flush.
    Argument: The set of card - hand
    Return:
    If True, Return (Rank:2, string), (Descending Order of Card Values)
    If False, Return False, None
    '''
    flu, _ = flush(hand)
    stra, num = straight(hand)
    if flu and stra:
        return (2, 'You are Amazing, its a "STRAIGHT FLUSH!!!!"(Rank:2)'), (num,)
    return False, None


def four_kind(hand: list) -> tuple:
    '''
    Check if hand is a Four of a Kind.
    Argument: The set of card - hand
    Return:
    If True, Return (Rank:3, string), (Card Value)
    If False, Return False, None
    '''
    val = [conv_card_to_num(x[0]) for x in hand]
    suit = [x[1] for x in hand]
    if len(set(suit)) != 4:
        return False, None
    dict_val = {i: val.count(i) for i in val}
    for k, v in dict_val.items():
        if v == 4:
            return (3, 'You have all suits of a card, "FOUR OF A KIND"(Rank:3)'), (k,)
    return False, None


def full_house(hand: list) -> tuple:
    '''
    Check if hand is a Full House.
    Argument: The set of card - hand
    Return:
    If True, Return (Rank:4, string), (Three Kind Card Value, Pair Card Value)
    If False, Return False, None
    '''
    thr, num_3 = three_kind(hand)
    op, num_2 = one_pair(hand)
    if thr and op:
        return (4, 'That is a "FULL HOUSE(Rank:4)"'), (num_3[0], num_2[0])
    return False, None


def flush(hand: list) -> tuple:
    '''
    Check if hand is a Flush.
    Argument: The set of card - hand
    Return:
    If True, Return (Rank:5, string), (Descending Order of Card Values)
    If False, Return False, None
    '''
    val = [conv_card_to_num(x[0]) for x in hand]
    val.sort()
    suit = [x[1] for x in hand]
    if len(set(suit)) != 1:
        return False, None
    return (5, 'You "FLUSHed it"(Rank:5)'), tuple(val[::-1])


def straight(hand: list) -> tuple:
    '''
    Check if hand is a Straight.
    Argument: The set of card - hand
    Return:
    If True, Return (Rank:6, string), (Descending Order of Card Values)
    If False, Return False, None
    '''
    val = [conv_card_to_num(x[0]) for x in hand]
    val.sort()
    k = 0
    for i in range(len(hand)-1):
        if val[i] == val[i+1]-1:
            k += 1
    if k == len(hand)-1:
        return (6, 'What a "STRAIGHT" drive(RANK:6)'), tuple(val[::-1])
    return False, None


def three_kind(hand: list) -> tuple:
    '''
    Check if hand is a Three of a Kind.
    Argument: The set of card - hand
    Return:
    If True, Return (Rank:7, string), (Three Kind Card Value,)
    If False, Return False, None
    '''
    val = [conv_card_to_num(x[0]) for x in hand]
    suit = [x[1] for x in hand]
    if len(set(suit)) < 3:
        return False, None
    dict_val = {i: val.count(i) for i in val}
    for k, v in dict_val.items():
        if v == 3:
            return (7, 'Go for 3, "THREE OF A KIND"(Rank:7)'), (k,)
    return False, None


def two_pair(hand: list) -> tuple:
    '''
    Check if hand is a Two Pairs.
    Argument: The set of card - hand
    Return:
    If True, Return (Rank:8, string), (Higher Pair Value, Lower Pair Value, Final Card Value)
    If False, Return False, None
    '''
    p1, n1 = one_pair(hand)
    if not p1:
        return False, None
    left_over_hand = [x for x in hand if conv_card_to_num(x[0]) != n1[0]]
    p2, n2 = one_pair(left_over_hand)
    if p1 and p2:
        final_card_val = [conv_card_to_num(
            x[0]) for x in left_over_hand if conv_card_to_num(x[0]) != n2[0]]
        return (8, 'This is good, "TWO PAIRS" haan (Rank:8)'), (max(n1[0], n2[0]), min(n1[0], n2[0]), *final_card_val)
    return False, None


def one_pair(hand: list) -> tuple:
    '''
    Check if hand is a One Pair.
    Argument: The set of card - hand
    Return:
    If True, Return (Rank:9, string), (Pair Card Value, Descending Order of Remaining Card Values)
    If False, Return False, None
    '''
    val = [conv_card_to_num(x[0]) for x in hand]
    val.sort()
    dict_val = {i: val.count(i) for i in val}
    for k, v in dict_val.items():
        if v == 2:
            left_over_val = [conv_card_to_num(
                x[0]) for x in hand if conv_card_to_num(x[0]) != k]
            left_over_val.sort()
            return (9, 'Good! It is a "PAIR"(Rank:9)'), (k, *left_over_val[::-1])
    return False, None


def high_card(hand: list) -> tuple:
    '''
    Argument: The set of card - hand
    Return:
    Return (Rank:10, string), (Descending Order of Card Values)
    '''
    val = [conv_card_to_num(x[0]) for x in hand]
    val.sort()
    return (10, f'Only hope is your High Card must be good enough(Rank:10)'), tuple(val[::-1])


def create_player(deck: list, cards_per_player: int = 5) -> tuple:
    '''
    Shuffles equal Cards to 2 players in a uniform sample way.
    Arguments:
        deck: Set of Cards
        card_per_player: Total number of cards for each player. Default:5
    Return:
        Tuple of set of card of each player.
    '''
    print('----SHUFFLING---')
    p1_hand = random.sample(tuple(deck), cards_per_player)
    p2_hand = random.sample(tuple(deck-set(p1_hand)), cards_per_player)
    print('----Lightening Speed Distribution Later---')
    print('Hey P1, you got: ', p1_hand)
    print('Hey P2, you got: ', p2_hand)
    print('------------------------------------------')

    return p1_hand, p2_hand


def winner(p1_hand: list, p2_hand: list) -> str:
    '''
    Determines the Winner of the POKER game.
    Arguments:
        p1_hand: List of card of Player 1
        p1_hand: List of card of Player 1
    Return:
        A Result of winner in formated string.
    '''
    win_cases = {
        5: [royal_flush, straight_flush, four_kind, full_house, flush, straight, three_kind, two_pair, one_pair, high_card],
        4: [royal_flush, straight_flush, four_kind, flush, straight, three_kind, two_pair, one_pair, high_card],
        3: [royal_flush, straight_flush, flush, straight, three_kind, one_pair, high_card]
    }
    if not isinstance(p1_hand, (list, tuple)):
        raise TypeError('Hand must be an iterable')
    if len(p1_hand) not in (3, 4, 5):
        raise ValueError("A Hand can have only 3/4/5 cards.")
    if len(p2_hand) not in (3, 4, 5):
        raise ValueError("A Hand can have only 3/4/5 cards.")
    if len(p1_hand) != len(p2_hand):
        raise ValueError('Unequal Number of Cards for P1 and P2')

    cards_per_player = len(p1_hand)
    win_case = win_cases[cards_per_player]
    p1_rank, p2_rank = int(), int()
    p1_stat, p2_stat = str(), str()
    p1_high, p2_high = int(), int()

    for case in win_case:
        if not p1_rank:
            p1_res = case(p1_hand)
            if p1_res[0]:
                p1_rank = p1_res[0][0]
                p1_stat = p1_res[0][1]
                p1_high = p1_res[1]
        if not p2_rank:
            p2_res = case(p2_hand)
            if p2_res[0]:
                p2_rank = p2_res[0][0]
                p2_stat = p2_res[0][1]
                p2_high = p2_res[1]

    print(f'Hey P1: {p1_stat}, with order of highest cards as: {p1_high}')
    print(f'Hey P2: {p2_stat}, with order of highest cards as: {p2_high}')
    print('------------------------------------------')
    if p1_rank < p2_rank:
        return f'Congratulations Player 1, you WON! as you had better hand.'
    elif p1_rank > p2_rank:
        return f'Congratulations Player 2, you WON! as you had better hand.'
    else:
        print('---TIE BREAKER CHECK:---')
        for p1_c, p2_c in zip(p1_high, p2_high):
            if p1_c > p2_c:
                return f'Congratulations Player 1, you have Won! as you had better high card {p1_c} than {p2_c}'
            elif p1_c < p2_c:
                return f'Congratulations Player 2, you have Won! as you had better high card {p2_c} than {p1_c}'
        else:
            return 'MAN....this is very rare....Its a TOTAL TIE!'


print(winner(*create_player(create_deck(vals, suits), 5)))
