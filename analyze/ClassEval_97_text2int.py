def text2int(self, textnum):
    """
    将单词字符串转换为相应的整数字符串
    :param textnum: 字符串，要转换的单词字符串
    :return: 字符串，最终转换的整数字符串
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
    
    # Split by spaces and hyphens
    words = textnum.replace("-", " ").split()
    
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
        elif word == "and":
            continue
    
    result += current
    return str(result)