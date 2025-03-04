def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    tags = set()
    result = text
    in_code_block = False
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        # Check for code block markers
        if line.strip().startswith('