def _normalizeargs(sequence, output=None):
    """
    घोषणा तर्कों को सामान्यीकृत करें

    सामान्यीकरण तर्कों में घोषणाएँ, ट्यूपल, या एकल इंटरफेस हो सकते हैं।

    व्यक्तिगत इंटरफेस या लागू विनिर्देशों को छोड़कर अन्य सभी का विस्तार किया जाएगा।
    """
    if output is None:
        output = []
    
    if isinstance(sequence, (list, tuple)):
        for item in sequence:
            _normalizeargs(item, output)
    else:
        output.append(sequence)
        
    return output