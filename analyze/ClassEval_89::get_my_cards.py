def get_my_cards(self):
        """
        Ottieni un elenco di quattro numeri casuali tra 1 e 9 che rappresentano le carte del giocatore.
        :return: elenco di interi, che rappresentano le carte del giocatore
        >>> gioco = TwentyFourPointGame()
        >>> gioco.get_my_cards()
        """
        self.nums = []
        self._generate_cards()
        return self.nums