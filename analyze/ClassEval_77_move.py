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
    # वर्तमान सिर की स्थिति प्राप्त करें
    current_head = self.positions[0]
    
    # नई सिर की स्थिति की गणना करें
    new_head = (current_head[0] + direction[0], current_head[1] + direction[1])
    
    # जांचें कि नया सिर भोजन की स्थिति पर है या नहीं
    if new_head == self.food_position:
        # भोजन खाएं
        self.positions.insert(0, new_head)
        self.length += 1
        self.score += 10
        # नया भोजन उत्पन्न करें (यदि food_position को अपडेट करने की आवश्यकता है)
        # self.generate_food() या इसी तरह का कोड
    # जांचें कि नया सिर शरीर से टकराता है या नहीं
    elif new_head in self.positions[1:]:
        # फिर से शुरू करें (रीसेट)
        self.reset()
    else:
        # सामान्य गति - सिर जोड़ें और पूंछ हटाएं
        self.positions.insert(0, new_head)
        self.positions.pop()