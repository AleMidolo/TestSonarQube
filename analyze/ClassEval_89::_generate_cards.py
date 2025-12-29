def _generate_cards(self):
    """
        Genera numeri casuali tra 1 e 9 per le carte.
        """
    self.nums = [random.randint(1, 9) for _ in range(4)]