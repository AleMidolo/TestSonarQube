def _create_in_regex(self) -> Pattern:
    """
    Create the in-style parameter regular expression.

    Returns the in-style parameter regular expression (:class:`re.Pattern`).
    """
    # Match parameters in the format {param_name}
    return re.compile(r'{([^{}]+)}')