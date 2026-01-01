def _generate_cards(self):
    """
        Generate random numbers between 1 and 9 for the cards.
        """
    self.nums = random.sample(range(1, 10), 4)