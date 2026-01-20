def text2int(self, textnum):
    """
    Convierte la cadena de palabras en la cadena de número entero correspondiente
    :param textnum: cadena, la cadena de palabras a ser convertida
    :return: cadena, la cadena de número entero final convertida
    >>> w2n = Words2Numbers()
    >>> w2n.text2int("thirty-two")
    "32"
    """
    ones = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
        "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
        "nineteen": 19
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
    
    textnum = textnum.lower().strip()
    
    if textnum in ones:
        return str(ones[textnum])
    
    words = textnum.replace("-", " ").split()
    
    current = 0
    result = 0
    
    for word in words:
        if word in ones:
            current += ones[word]
        elif word in tens:
            current += tens[word]
        elif word == "hundred":
            current *= 100
        elif word in scales:
            current *= scales[word]
            result += current
            current = 0
    
    result += current
    
    return str(result)