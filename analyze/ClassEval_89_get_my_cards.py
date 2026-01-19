import random

def get_my_cards(self):
    """
    1 से 9 के बीच चार यादृच्छिक संख्याओं की एक सूची प्राप्त करें जो खिलाड़ी के कार्ड का प्रतिनिधित्व करती हैं।
    :return: पूर्णांकों की सूची, जो खिलाड़ी के कार्ड का प्रतिनिधित्व करती है
    >>> game = TwentyFourPointGame()
    >>> game.get_my_cards()

    """
    return [random.randint(1, 9) for _ in range(4)]