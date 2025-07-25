def validate_choices_args(self, args):
    """
    चॉइस आर्ग्युमेंट्स का मान उपलब्ध विकल्पों में से एक है या नहीं, इसकी जांच करें।

    :param args: प्राप्त किए गए आर्ग्युमेंट्स।
    """
    valid_choices = ["option1", "option2", "option3"]  # उपलब्ध विकल्पों की सूची
    for arg in args:
        if arg not in valid_choices:
            raise ValueError(f"अमान्य विकल्प: {arg}")
    return True