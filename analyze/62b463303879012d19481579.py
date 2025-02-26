def _extract_number_and_supplment_from_issue_element(issue):
    """
    从 issue 的内容中返回 number 和 sup 的可能值。
    从 issue 的内容中提取 number 和 suppl 的可能值。
    """
    import re

    # Initialize variables to hold the extracted values
    number = None
    suppl = None

    # Use regex to find the number and suppl in the issue content
    number_match = re.search(r'number\s*:\s*(\d+)', issue, re.IGNORECASE)
    suppl_match = re.search(r'suppl\s*:\s*([^\s,]+)', issue, re.IGNORECASE)

    if number_match:
        number = number_match.group(1)
    
    if suppl_match:
        suppl = suppl_match.group(1)

    return number, suppl