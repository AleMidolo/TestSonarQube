import re

def regex_dict(item):
    """
    *.cpp कुंजियों को regex कुंजियों में बदलें

    एक dict दिया गया है जिसमें सभी कुंजियाँ वाइल्डकार्ड के साथ फ़ाइल नाम हैं,
    केवल कुंजियों को उनके समकक्ष regex में बदलें और मानों को वैसा ही छोड़ दें।

    उदाहरण:

    नियम (rules) = {
        '*.cpp':
            {'a': 'arf', 'b': 'bark', 'c': 'coo'},
        '*.h':
            {'h': 'help'}
    }
    regex_keys = regex_dict(rules)

    आर्ग्युमेंट्स:
        item: वह dict जिसे बदलना है
    रिटर्न करता है:
        एक dict जिसमें कुंजियाँ regex में परिवर्तित होती हैं
    """
    regex_dict = {}
    for key, value in item.items():
        # Convert wildcard '*' to regex equivalent
        regex_key = re.escape(key).replace(r'\*', '.*')
        regex_dict[regex_key] = value
    return regex_dict