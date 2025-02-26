def _extract_number_and_supplment_from_issue_element(issue):
    """
    从 issue 的内容中返回 number 和 sup 的可能值。
    从 issue 的内容中提取 number 和 suppl 的可能值。
    """
    import re

    number_pattern = r'(?<=#)\d+'
    suppl_pattern = r'\b(?:sup|supplement)\s*[:\-]?\s*(\w+)\b'

    number_matches = re.findall(number_pattern, issue)
    suppl_matches = re.findall(suppl_pattern, issue, re.IGNORECASE)

    number = number_matches[0] if number_matches else None
    suppl = suppl_matches[0] if suppl_matches else None

    return number, suppl