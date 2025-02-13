def validate_length_args(self, args):
    max_length = 10  # Specify the maximum length
    for arg in args:
        if len(arg) > max_length:
            return False
    return True