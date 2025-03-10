import re

def _create_in_regex(self) -> Pattern:
    """
    Create the in-style parameter regular expression.

    Returns the in-style parameter regular expression (:class:`re.Pattern`).
    """
    return re.compile(r'\bIN\s*\(\s*([^)]+)\s*\)', re.IGNORECASE)