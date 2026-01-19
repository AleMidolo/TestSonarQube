def level_up(self):
    """
    पात्र का स्तर बढ़ाएं और अनुभव अंक को शून्य पर वापस लाएं, स्वास्थ्य (hp) में 20 अंक बढ़ाएं, हमले की शक्ति और रक्षा अंक में 5 अंक बढ़ाएं।
    अधिकतम स्तर 100 है।
    :return: tuple[int, int, int, int], नए स्तर, स्वास्थ्य अंक, हमले की शक्ति, और स्तर बढ़ाने के बाद रक्षा अंक।
    >>> player_1 = RPGCharacter('खिलाड़ी 1', 100, 10, 3)
    >>> player_1.level_up()
    (2, 120, 15, 8)
    """
    # Only level up if current level is below 100
    if self.level < 100:
        self.level += 1
    
    # Reset experience points to zero
    self.experience = 0
    
    # Increase health by 20
    self.hp += 20
    
    # Increase attack power by 5
    self.attack += 5
    
    # Increase defense by 5
    self.defense += 5
    
    return (self.level, self.hp, self.attack, self.defense)