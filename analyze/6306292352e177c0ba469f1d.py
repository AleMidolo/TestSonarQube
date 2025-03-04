def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    """
    Find tags in text.
    
    Tries to ignore tags inside code blocks.
    
    Optionally, if passed a "replacer", will also replace the tag word with the result
    of the replacer function called with the tag word.
    
    Returns a set of tags and the original or replaced text.
    """
    tags = set()
    result_text = text
    in_code_block = False
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        # Check for code block markers
        if line.strip().startswith('