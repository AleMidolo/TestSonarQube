def validate_choices_args(self, args):
    """
    चॉइस आर्ग्युमेंट्स का मान उपलब्ध विकल्पों में से एक है या नहीं, इसकी जांच करें।

    :param args: प्राप्त किए गए आर्ग्युमेंट्स।
    """
    if not hasattr(self, 'choices'):
        raise AttributeError("No choices defined for validation.")
    
    if not isinstance(args, (list, tuple)):
        args = [args]
    
    for arg in args:
        if arg not in self.choices:
            raise ValueError(f"Invalid choice: {arg}. Valid choices are: {self.choices}")
    
    return True