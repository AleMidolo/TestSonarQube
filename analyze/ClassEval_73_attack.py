def attack(self, other_character):
    """
    Attacca un altro personaggio. Il danno causato deve compensare il valore di difesa.
    :param other_character: str, Il personaggio che viene attaccato.
    >>> player_1 = RPGCharacter('giocatore 1', 100, 10, 3)
    >>> player_2 = RPGCharacter('giocatore 2', 100, 7, 2)
    >>> player_1.attack(player_2)
    >>> player_2.hp
    92
    """
    damage = max(0, self.attack_power - other_character.defense)
    other_character.hp -= damage