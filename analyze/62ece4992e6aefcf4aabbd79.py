import re

def make_find_paths(find_paths):
    """
    Given a sequence of path fragments or patterns as passed to `--find`, transform all path
    fragments into glob patterns. Pass through existing patterns untouched.

    For example, given find_paths of:

      ['foo.txt', 'pp:root/somedir']

    ... transform that into:

      ['sh:**/*foo.txt*/**', 'pp:root/somedir']
    """
    transformed_paths = []
    for path in find_paths:
        if re.match(r'^[a-zA-Z]+:', path):
            # Pass through existing patterns untouched
            transformed_paths.append(path)
        else:
            # Transform path fragments into glob patterns
            transformed_paths.append(f'sh:**/*{path}*/**')
    return transformed_paths