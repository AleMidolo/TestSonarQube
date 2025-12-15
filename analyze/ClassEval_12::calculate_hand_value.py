def calculate_hand_value(self, hand):
        """
        हाथ सूची में संग्रहीत पोकर कार्डों का मूल्य Blackjack खेल के नियमों के अनुसार गणना करें।
        यदि कार्ड एक अंक है, तो इसका मूल्य कुल हाथ के मूल्य में जोड़ा जाता है।
        J, Q, या K का मूल्य 10 है, जबकि एसेस का मूल्य 11 है।
        यदि कुल हाथ का मूल्य 21 से अधिक हो जाता है और एसेस मौजूद हैं, तो एक एसेस को 11 के बजाय 1 के मूल्य के रूप में माना जाता है,
        जब तक हाथ का मूल्य 21 से कम या उसके बराबर नहीं हो जाता, या सभी एसेस को 1 के मूल्य के रूप में नहीं गिना जाता।
        :param hand: सूची
        :return: हाथ सूची में संग्रहीत पोकर कार्डों का मूल्य, एक संख्या।
        >>> black_jack_game.calculate_hand_value(['QD', '9D', 'JC', 'QH', 'AS'])
        40
        """
        value = 0
        aces = 0
        
        for card in hand:
            rank = card[:-1]  # Get the rank of the card
            if rank in ['J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                aces += 1
                value += 11  # Initially count Ace as 11
            else:
                value += int(rank)  # Add the numeric value of the card
        
        # Adjust for Aces if value exceeds 21
        while value > 21 and aces:
            value -= 10  # Count one Ace as 1 instead of 11
            aces -= 1
        
        return value