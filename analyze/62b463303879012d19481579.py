def _extract_number_and_supplment_from_issue_element(issue):
    """
    Extract the possible values of number and suppl from the contents of issue.
    """
    number = None
    suppl = None
    
    if issue is not None:
        issue_text = issue.strip()
        if issue_text:
            # Check if the issue contains a supplement (e.g., "Suppl 1" or "S1")
            if "Suppl" in issue_text:
                parts = issue_text.split("Suppl")
                number = parts[0].strip()
                suppl = "Suppl" + parts[1].strip()
            elif "S" in issue_text and issue_text.index("S") == 0:
                parts = issue_text.split("S")
                number = parts[0].strip()
                suppl = "S" + parts[1].strip()
            else:
                number = issue_text
    
    return number, suppl