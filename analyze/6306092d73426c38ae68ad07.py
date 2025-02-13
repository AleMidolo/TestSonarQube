def validate_requires_args(self, args):
    required_args = self.get_required_args()
    missing_args = [arg for arg in required_args if arg not in args]
    if missing_args:
        raise ValueError(f"Missing required arguments: {', '.join(missing_args)}")