def _generate_cards(self):
    """
        Genera numeri casuali tra 1 e 9 per le carte.
        """
    self.nums = random.sample(range(1, 10), 4)