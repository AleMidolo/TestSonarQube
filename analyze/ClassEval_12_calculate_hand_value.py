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
    total_value = 0
    ace_count = 0
    
    for card in hand:
        # Extract the rank (first character(s) of the card)
        rank = card[:-1]  # All characters except the last one (suit)
        
        if rank == 'A':
            ace_count += 1
            total_value += 11
        elif rank in ['J', 'Q', 'K']:
            total_value += 10
        else:
            total_value += int(rank)
    
    # Adjust for aces if total_value > 21
    while total_value > 21 and ace_count > 0:
        total_value -= 10  # Convert an ace from 11 to 1
        ace_count -= 1
    
    return total_value