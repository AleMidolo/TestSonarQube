def calculate_hand_value(self, hand):
    """
    Calculate the value of the poker cards stored in hand list according to the rules of the Blackjack Game.
    If the card is a digit, its value is added to the total hand value.
    Value of J, Q, or K is 10, while Aces are worth 11.
    If the total hand value exceeds 21 and there are Aces present, one Ace is treated as having a value of 1 instead of 11,
    until the hand value is less than or equal to 21, or all Aces have been counted as value of 1.
    :param hand: list
    :return: the value of the poker cards stored in hand list, a number.
    >>> black_jack_game.calculate_hand_value(['QD', '9D', 'JC', 'QH', 'AS'])
    40
    """
    total_value = 0
    ace_count = 0
    
    for card in hand:
        # Extract the rank (first character(s) of the card)
        rank = card[:-1]  # All characters except the last one (suit)
        
        if rank == 'A':
            total_value += 11
            ace_count += 1
        elif rank in ['J', 'Q', 'K']:
            total_value += 10
        else:
            total_value += int(rank)
    
    # Adjust for Aces if total exceeds 21
    while total_value > 21 and ace_count > 0:
        total_value -= 10  # Convert an Ace from 11 to 1
        ace_count -= 1
    
    return total_value