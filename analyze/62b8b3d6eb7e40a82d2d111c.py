def _normalizeargs(sequence, output=None):
    """
    घोषणा तर्कों को सामान्यीकृत करें

    सामान्यीकरण तर्कों में घोषणाएँ, ट्यूपल, या एकल इंटरफेस हो सकते हैं।

    व्यक्तिगत इंटरफेस या लागू विनिर्देशों को छोड़कर अन्य सभी का विस्तार किया जाएगा।
    """
    if isinstance(sequence, (list, tuple)):
        return [(_normalizeargs(item, output) if isinstance(item, (list, tuple)) else item) for item in sequence]
    elif isinstance(sequence, dict):
        return {key: _normalizeargs(value, output) for key, value in sequence.items()}
    elif hasattr(sequence, '__iter__') and not isinstance(sequence, str):
        return list(map(lambda x: _normalizeargs(x, output), sequence))
    else:
        return sequence