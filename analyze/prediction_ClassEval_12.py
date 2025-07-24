import random


class BlackjackGame:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        return self.shuffle_deck(self.build_deck())

    def build_deck(self):
        suits = ['S', 'C', 'D', 'H']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return [rank + suit for suit in suits for rank in ranks]

    def shuffle_deck(self, deck):
        random.shuffle(deck)
        return deck

    def calculate_hand_value(self, hand):
        value, num_aces = self.calculate_base_hand_value(hand)
        return self.adjust_for_aces(value, num_aces)

    def calculate_base_hand_value(self, hand):
        value = 0
        num_aces = 0
        for card in hand:
            rank = card[:-1]
            if rank.isdigit():
                value += int(rank)
            elif rank in ['J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                value += 11
                num_aces += 1
        return value, num_aces

    def adjust_for_aces(self, value, num_aces):
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1
        return value

    def check_winner(self):
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)
        return self.determine_winner(player_value, dealer_value)

    def determine_winner(self, player_value, dealer_value):
        if player_value > 21 and dealer_value > 21:
            return 'Dealer wins' if player_value > dealer_value else 'Player wins'
        elif player_value > 21:
            return 'Dealer wins'
        elif dealer_value > 21:
            return 'Player wins'
        else:
            return 'Dealer wins' if player_value <= dealer_value else 'Player wins'