import random

def create_deck(self):
    """
    创建一副52张牌的牌组,包含除了小丑牌以外的52张随机顺序的扑克牌。
    :return: 一个包含52张随机顺序的扑克牌的列表,格式为 ['AS', '2S', ...]。
    """
    # 定义花色和牌面值
    suits = ['S', 'H', 'D', 'C']  # Spades, Hearts, Diamonds, Clubs
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    # 创建一副完整的牌
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    
    # 随机打乱牌组
    random.shuffle(deck)
    
    return deck