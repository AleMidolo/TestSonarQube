def text2int(self, textnum):
    """
    शब्द स्ट्रिंग को संबंधित पूर्णांक स्ट्रिंग में परिवर्तित करें
    :param textnum: स्ट्रिंग, परिवर्तित करने के लिए शब्द स्ट्रिंग
    :return: स्ट्रिंग, अंतिम परिवर्तित पूर्णांक स्ट्रिंग
    >>> w2n = Words2Numbers()
    >>> w2n.text2int("thirty-two")
    "32"
    """
    ones = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19
    }
    
    tens = {
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }
    
    scales = {
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000,
        "billion": 1000000000,
        "trillion": 1000000000000
    }
    
    textnum = textnum.lower().replace(" and ", " ").replace("-", " ")
    words = textnum.split()
    
    current = 0
    result = 0
    
    for word in words:
        if word in ones:
            current += ones[word]
        elif word in tens:
            current += tens[word]
        elif word in scales:
            if word == "hundred":
                current *= scales[word]
            else:
                current *= scales[word]
                result += current
                current = 0
    
    result += current
    return str(result)