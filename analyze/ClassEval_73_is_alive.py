def is_alive(self):
    """
    जांचें कि खिलाड़ी जीवित है या नहीं।
    :return: यदि hp 0 से बड़ा है तो True, अन्यथा False।
    >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
    >>> player_1.is_alive()
    True
    """
    return self.hp > 0