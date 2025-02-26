def validate_choices_args(self, args):
    """
    चॉइस आर्ग्युमेंट्स का मान उपलब्ध विकल्पों में से एक है या नहीं, इसकी जांच करें।

    :param args: प्राप्त किए गए आर्ग्युमेंट्स।
    """
    available_choices = self.get_available_choices()  # Assuming this method exists
    if args not in available_choices:
        raise ValueError(f"Invalid choice: {args}. Available choices are: {available_choices}")