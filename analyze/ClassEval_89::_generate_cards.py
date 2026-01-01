def _generate_cards(self):
    """
        Generate random numbers between 1 and 9 for the cards.
        """
    self.nums = [random.randint(1, 9) for _ in range(4)]