def display(self, key, value):
    """
    निम्नलिखित प्रारूप के साथ कॉर्ड प्रिंट करें और धुन बजाएं: सामान्य गिटार खेलने का तरीका -- कॉर्ड: %s, धुन बजाएं: %s
    :param key:str, कॉर्ड
    :param value:str, धुन बजाएं
    :return: str
    >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
    >>> context.display("C", "53231323")
    सामान्य गिटार खेलने का तरीका -- कॉर्ड: C, धुन बजाएं: 53231323

    """
    result = f"सामान्य गिटार खेलने का तरीका -- कॉर्ड: {key}, धुन बजाएं: {value}"
    print(result)
    return result