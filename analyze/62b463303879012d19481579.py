def _extract_number_and_supplment_from_issue_element(issue):
    """
    从 issue 的内容中返回 number 和 sup 的可能值。
    从 issue 的内容中提取 number 和 suppl 的可能值。
    """
    import re

    number_pattern = r'(?<=#)\d+'
    suppl_pattern = r'\b(sup|supplement|supp)\s*:\s*(\w+)\b'

    number_match = re.search(number_pattern, issue)
    suppl_match = re.search(suppl_pattern, issue, re.IGNORECASE)

    number = number_match.group(0) if number_match else None
    suppl = suppl_match.group(2) if suppl_match else None

    return number, suppl