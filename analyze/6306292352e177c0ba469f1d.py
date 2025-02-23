from typing import Tuple, Set
import re

def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    """
    Find tags in text.

    Tries to ignore tags inside code blocks.

    Optionally, if passed a "replacer", will also replace the tag word with the result
    of the replacer function called with the tag word.

    Returns a set of tags and the original or replaced text.
    """
    # Regex to find code blocks
    code_block_pattern = r'