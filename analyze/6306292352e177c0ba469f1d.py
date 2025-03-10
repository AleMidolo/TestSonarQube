from typing import Set, Tuple, Callable
import re

def find_tags(text: str, replacer: Callable = None) -> Tuple[Set, str]:
    """
    Find tags in text.

    Tries to ignore tags inside code blocks.

    Optionally, if passed a "replacer", will also replace the tag word with the result
    of the replacer function called with the tag word.

    Returns a set of tags and the original or replaced text.
    """
    # Regular expression to match tags (words starting with #)
    tag_pattern = re.compile(r'#\w+')
    
    # Regular expression to match code blocks (