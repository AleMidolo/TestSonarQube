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
    # सांप के सिर की वर्तमान स्थिति प्राप्त करें
    current_head = self.positions[0]
    
    # नई स्थिति की गणना करें
    new_head = (current_head[0] + direction[0], current_head[1] + direction[1])
    
    # नए सिर को positions की शुरुआत में जोड़ें
    self.positions.insert(0, new_head)
    
    # जांचें कि क्या सांप ने भोजन खा लिया
    if hasattr(self, 'food_position') and new_head == self.food_position:
        # भोजन खा लिया - लंबाई बढ़ाएं और स्कोर बढ़ाएं
        self.length += 1
        self.score += 10
        # नया भोजन उत्पन्न करें (यदि food generation method है)
        if hasattr(self, 'generate_food'):
            self.generate_food()
    # जांचें कि क्या सांप ने खुद से टकराया
    elif new_head in self.positions[1:]:
        # खुद से टकराया - गेम रीसेट करें
        if hasattr(self, 'reset'):
            self.reset()
        else:
            # मैनुअल रीसेट
            self.length = 1
            self.positions = [new_head]
            self.score = 0
    else:
        # सामान्य चाल - पूंछ हटाएं
        self.positions.pop()