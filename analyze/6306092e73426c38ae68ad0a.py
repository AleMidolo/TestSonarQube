def validate_choices_args(self, args):
    """
    चॉइस आर्ग्युमेंट्स का मान उपलब्ध विकल्पों में से एक है या नहीं, इसकी जांच करें।

    :param args: प्राप्त किए गए आर्ग्युमेंट्स।
    """
    for arg_name, arg_value in args.items():
        if hasattr(self, f'_{arg_name}_choices'):
            choices = getattr(self, f'_{arg_name}_choices')
            if arg_value not in choices:
                raise ValueError(f"Invalid value '{arg_value}' for argument '{arg_name}'. "
                               f"Allowed values are: {choices}")