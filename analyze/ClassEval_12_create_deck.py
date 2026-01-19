import random

def create_deck(self):
    """
    Crea un mazzo di 52 carte, che memorizza 52 poker in ordine casuale con i jolly rimossi.
    :return: una lista di 52 poker in ordine casuale con i jolly rimossi, il formato è ['AS', '2S', ...].
    """
    # Define the ranks and suits
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['S', 'H', 'D', 'C']  # Spades, Hearts, Diamonds, Clubs
    
    # Create the deck by combining each rank with each suit
    deck = [rank + suit for suit in suits for rank in ranks]
    
    # Shuffle the deck to randomize the order
    random.shuffle(deck)
    
    return deck