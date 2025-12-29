def __format_line_feed(self, text):
    """
        लगातार लाइन ब्रेक को एकल लाइन ब्रेक से बदलें
        :param text: लगातार लाइन ब्रेक के साथ स्ट्रिंग
        :return: स्ट्रिंग, एकल लाइन ब्रेक के साथ बदला हुआ टेक्स्ट
        """
    if not text:
        return text
    formatted_text = re.sub('[\\r\\n]+', '\n', text)
    formatted_text = formatted_text.strip()
    return formatted_text