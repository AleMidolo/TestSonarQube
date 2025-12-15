def _generate_cards(self):
    """
    Generate four random numbers between 1 and 9 for the player's cards.
    """
    self.nums = random.sample(range(1, 10), 4)