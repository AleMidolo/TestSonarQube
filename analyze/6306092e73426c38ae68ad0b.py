def validate_min_max_args(self, args):
    """
    जांचें कि आर्ग्युमेंट्स का मान न्यूनतम और अधिकतम मानों के बीच है या नहीं।

    :param args: प्राप्त किए गए आर्ग्युमेंट्स।
    """
    for arg_name, arg_value in args.items():
        if hasattr(self, f'min_{arg_name}') and hasattr(self, f'max_{arg_name}'):
            min_val = getattr(self, f'min_{arg_name}')
            max_val = getattr(self, f'max_{arg_name}')
            
            if not (min_val <= arg_value <= max_val):
                raise ValueError(f'{arg_name} का मान {min_val} और {max_val} के बीच होना चाहिए')