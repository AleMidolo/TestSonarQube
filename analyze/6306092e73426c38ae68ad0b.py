def validate_min_max_args(self, args):
    min_value = self.min_value
    max_value = self.max_value
    return all(min_value <= arg <= max_value for arg in args)