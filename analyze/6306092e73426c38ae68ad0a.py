def validate_choices_args(self, args):
    """
    चॉइस आर्ग्युमेंट्स का मान उपलब्ध विकल्पों में से एक है या नहीं, इसकी जांच करें।

    :param args: प्राप्त किए गए आर्ग्युमेंट्स।
    """
    for arg_name, arg_value in args.items():
        if hasattr(self, 'choices') and arg_name in self.choices:
            valid_choices = self.choices[arg_name]
            if arg_value not in valid_choices:
                raise ValueError(f"Argument '{arg_name}' must be one of {valid_choices}. Got '{arg_value}'")