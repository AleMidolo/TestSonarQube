def gain_exp(self, amount):
    """
        चरित्र के लिए अनुभव अंक प्राप्त करें और जब अनुभव वर्तमान स्तर का 100 गुना हो जाए तो स्तर बढ़ाएं
        जो अनुभव ओवरफ्लो होता है उसका उपयोग अगले स्तर के लिए गणना करने के लिए किया जाना चाहिए जब तक कि यह समाप्त न हो जाए
        :param amount: int, प्राप्त करने के लिए अनुभव अंकों की मात्रा।
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.gain_exp(1100)
        >>> player_1.exp
        100
        >>> player_1.level
        5
        """
    self.exp += amount
    while self.level < 100 and self.exp >= self.level * 100:
        self.exp -= self.level * 100
        self.level += 1
        self.hp += 20
        self.attack_power += 5
        self.defense += 5
    if self.level >= 100:
        self.exp = 0