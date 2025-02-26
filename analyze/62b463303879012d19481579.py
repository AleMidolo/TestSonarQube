def _extract_number_and_supplment_from_issue_element(issue):
    """
    समस्या (issue) की सामग्री से number और suppl के संभावित मानों को निकालें।
    """
    import re

    # Regular expressions to find number and supplement
    number_pattern = r'\b\d+\b'
    suppl_pattern = r'\b[A-Za-z]+\b'

    # Extracting number
    number_match = re.search(number_pattern, issue)
    number = number_match.group(0) if number_match else None

    # Extracting supplement
    suppl_matches = re.findall(suppl_pattern, issue)
    suppl = suppl_matches[1] if len(suppl_matches) > 1 else None  # Assuming the second match is the supplement

    return number, suppl