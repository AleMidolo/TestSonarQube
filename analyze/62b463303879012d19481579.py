def _extract_number_and_supplment_from_issue_element(issue):
    """
    समस्या (issue) की सामग्री से number और suppl के संभावित मानों को निकालें।
    """
    number = None
    suppl = None
    
    if issue:
        # Remove any whitespace
        issue = issue.strip()
        
        # Check if issue contains supplement indicator
        if 'suppl' in issue.lower():
            parts = issue.lower().split('suppl')
            if parts[0]:
                number = parts[0].strip()
            if len(parts) > 1:
                suppl = parts[1].strip()
        else:
            # If no supplement, treat entire string as number
            number = issue
            
        # Clean up number - remove any non-numeric characters
        if number:
            number = ''.join(c for c in number if c.isdigit())
            if not number:
                number = None
                
        # Clean up supplement - remove any non-alphanumeric characters
        if suppl:
            suppl = ''.join(c for c in suppl if c.isalnum())
            if not suppl:
                suppl = None
    
    return number, suppl