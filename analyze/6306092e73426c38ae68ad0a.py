def validate_choices_args(self, args):
    available_choices = ['choice1', 'choice2', 'choice3']  # Example choices
    for arg in args:
        if arg not in available_choices:
            return False
    return True