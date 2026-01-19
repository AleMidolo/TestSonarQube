def move(self, direction):
    """
        निर्दिष्ट दिशा में सांप को चलाएं। यदि सांप के सिर की नई स्थिति भोजन की स्थिति के बराबर है, तो भोजन खा लें; यदि सांप के सिर की स्थिति उसके शरीर की स्थिति के बराबर है, तो फिर से शुरू करें, अन्यथा इसकी अपनी लंबाई में एक जोड़ें।
        :param direction: tuple, जो गति की दिशा का प्रतिनिधित्व करता है (x, y)।
        :return: None
        >>> snake.move((1,1))
        self.length = 1
        self.positions = [(51, 51), (50, 50)]
        self.score = 10
        """
    new_head = (self.positions[0][0] + direction[0] * self.BLOCK_SIZE, self.positions[0][1] + direction[1] * self.BLOCK_SIZE)
    if new_head == self.food_position:
        self.eat_food()
    elif new_head in self.positions:
        self.reset()
    else:
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()