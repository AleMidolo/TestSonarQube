import random

def create_deck(self):
    """
    52 कार्ड का एक डेक बनाएं, जिसमें 52 रैंडम तरीके से ऑर्डर किए गए पोकर कार्ड स्टोर हों, जिसमें से जोकर हटा दिए गए हों।

    :return: 52 रैंडम तरीके से ऑर्डर किए गए पोकर कार्ड की एक लिस्ट, जिसमें से जोकर हटा दिए गए हों, 
             इस फ़ॉर्मेट में ['AS', '2S', ...]।

    >>> black_jack_game = BlackjackGame()
    >>> black_jack_game.create_deck()
    ['QD', '9D', 'JC', 'QH', '2S', 'JH', '7D', '6H', '9S', '5C', '7H', 'QS',
     '5H', '6C', '7C', '3D', '10C', 'AD', '4C', '5D', 'AH', '2D', 'QC', 'KH',
     '9C', '9H', '4H', 'JS', '6S', '8H', '8C', '4S', '3H', '10H', '7S', '6D',
     '3C', 'KC', '3S', '2H', '10D', 'KS', '4D', 'AC', '10S', '2C', 'KD', '5S',
     'JD', '8S', 'AS', '8D']
    """
    # Define ranks and suits
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['S', 'H', 'D', 'C']  # Spades, Hearts, Diamonds, Clubs
    
    # Create deck with all combinations
    deck = [rank + suit for suit in suits for rank in ranks]
    
    # Shuffle the deck randomly
    random.shuffle(deck)
    
    return deck