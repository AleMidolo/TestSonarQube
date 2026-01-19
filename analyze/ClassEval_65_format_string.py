def format_string(self, x):
    """
    एक संख्या के स्ट्रिंग प्रतिनिधित्व को शब्दों के प्रारूप में परिवर्तित करता है
    :param x: str, संख्या का स्ट्रिंग प्रतिनिधित्व
    :return: str, संख्या शब्दों के प्रारूप में
    >>> formatter = NumberWordFormatter()
    >>> formatter.format_string("123456")
    "एक सौ और तेईस हजार चार सौ और छप्पन केवल"
    """
    # Hindi number words mapping
    ones = ["", "एक", "दो", "तीन", "चार", "पांच", "छह", "सात", "आठ", "नौ"]
    teens = ["दस", "ग्यारह", "बारह", "तेरह", "चौदह", "पंद्रह", "सोलह", "सत्रह", "अठारह", "उन्नीस"]
    twenties = ["", "", "बीस", "तीस", "चालीस", "पचास", "साठ", "सत्तर", "अस्सी", "नब्बे"]
    
    # Special two-digit numbers (21-99)
    two_digit_special = {
        21: "इक्कीस", 22: "बाईस", 23: "तेईस", 24: "चौबीस", 25: "पच्चीस",
        26: "छब्बीस", 27: "सत्ताईस", 28: "अट्ठाईस", 29: "उनतीस",
        31: "इकतीस", 32: "बत्तीस", 33: "तैंतीस", 34: "चौंतीस", 35: "पैंतीस",
        36: "छत्तीस", 37: "सैंतीस", 38: "अड़तीस", 39: "उनतालीस",
        41: "इकतालीस", 42: "बयालीस", 43: "तैंतालीस", 44: "चौवालीस", 45: "पैंतालीस",
        46: "छियालीस", 47: "सैंतालीस", 48: "अड़तालीस", 49: "उनचास",
        51: "इक्यावन", 52: "बावन", 53: "तिरपन", 54: "चौवन", 55: "पचपन",
        56: "छप्पन", 57: "सत्तावन", 58: "अट्ठावन", 59: "उनसठ",
        61: "इकसठ", 62: "बासठ", 63: "तिरसठ", 64: "चौंसठ", 65: "पैंसठ",
        66: "छियासठ", 67: "सड़सठ", 68: "अड़सठ", 69: "उनहत्तर",
        71: "इकहत्तर", 72: "बहत्तर", 73: "तिहत्तर", 74: "चौहत्तर", 75: "पचहत्तर",
        76: "छिहत्तर", 77: "सतहत्तर", 78: "अठहत्तर", 79: "उन्यासी",
        81: "इक्यासी", 82: "बयासी", 83: "तिरासी", 84: "चौरासी", 85: "पचासी",
        86: "छियासी", 87: "सत्तासी", 88: "अट्ठासी", 89: "नवासी",
        91: "इक्यानवे", 92: "बानवे", 93: "तिरानवे", 94: "चौरानवे", 95: "पचानवे",
        96: "छियानवे", 97: "सत्तानवे", 98: "अट्ठानवे", 99: "निन्यानवे"
    }
    
    def convert_two_digit(n):
        if n == 0:
            return ""
        elif n < 10:
            return ones[n]
        elif n < 20:
            return teens[n - 10]
        elif n in two_digit_special:
            return two_digit_special[n]
        else:
            return twenties[n // 10] + (ones[n % 10] if n % 10 != 0 else "")
    
    def convert_hundreds(n):
        if n == 0:
            return ""
        result = []
        hundreds = n // 100
        remainder = n % 100
        
        if hundreds > 0:
            result.append(ones[hundreds] + " सौ")
        
        if remainder > 0:
            if hundreds > 0:
                result.append("और")
            result.append(convert_two_digit(remainder))
        
        return " ".join(result)
    
    num = int(x)
    if num == 0:
        return "शून्य केवल"
    
    result = []
    
    # Handle lakhs (100000s)
    lakhs = num // 100000
    if lakhs > 0:
        result.append(convert_hundreds(lakhs) + " लाख")
        num %= 100000
    
    # Handle thousands (1000s)
    thousands = num // 1000
    if thousands > 0:
        result.append(convert_hundreds(thousands) + " हजार")
        num %= 1000
    
    # Handle remaining hundreds
    if num > 0:
        result.append(convert_hundreds(num))
    
    return " ".join(result) + " केवल"