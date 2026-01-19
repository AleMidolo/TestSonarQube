def _generate_cards(self):
    """
        कार्डों के लिए 1 और 9 के बीच यादृच्छिक संख्याएँ उत्पन्न करें।
        """
    self.nums = [random.randint(1, 9) for _ in range(4)]