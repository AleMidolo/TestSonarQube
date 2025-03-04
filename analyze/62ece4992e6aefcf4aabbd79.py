def make_find_paths(find_paths):
    """
    `--find` के लिए पास किए गए पथ खंडों (path fragments) या पैटर्न के अनुक्रम को लें और सभी पथ खंडों को ग्लोब पैटर्न में बदलें। मौजूदा पैटर्न को बिना बदले पास करें।
    """
    result = []
    for path in find_paths:
        # Check if path is already a pattern (starts with pp:)
        if path.startswith('pp:'):
            result.append(path)
        else:
            # Convert path fragment to glob pattern
            # Add **/* prefix and */** suffix to match anywhere in path
            glob_pattern = f'sh:**/*{path}*/**'
            result.append(glob_pattern)
    return result