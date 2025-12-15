def validate_phone_number(self, phone_number):
        """
        फोन नंबर की वैधता की पुष्टि करें
        :param phone_number: पुष्टि करने के लिए फोन नंबर
        :return: True या False, यह दर्शाते हुए कि फोन नंबर वैध है या नहीं
        >>> ru = RegexUtils()
        >>> ru.validate_phone_number("123-456-7890")
        True
        """
        pattern = self.generate_phone_number_pattern()
        return self.match(pattern, phone_number)