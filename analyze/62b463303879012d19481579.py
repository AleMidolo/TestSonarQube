def _extract_number_and_supplment_from_issue_element(issue):
    """
    समस्या (issue) की सामग्री से number और suppl के संभावित मानों को निकालें।
    
    Args:
        issue (str): समस्या की सामग्री जिसमें से number और suppl निकालना है।
    
    Returns:
        tuple: (number, suppl) के रूप में एक tuple जहां number और suppl संभावित मान हैं।
              यदि कोई मान नहीं मिलता है, तो None लौटाया जाएगा।
    """
    number = None
    suppl = None
    
    # यहां हम समस्या की सामग्री से number और suppl निकालने के लिए कुछ तर्क लागू करेंगे।
    # उदाहरण के लिए, यदि समस्या की सामग्री में "No. 123" और "Suppl. 4" है, तो:
    # number = 123, suppl = 4
    
    # यह एक उदाहरण है, आप इसे अपनी आवश्यकताओं के अनुसार संशोधित कर सकते हैं।
    if "No." in issue:
        number_part = issue.split("No.")[1].split()[0]
        number = int(number_part) if number_part.isdigit() else None
    
    if "Suppl." in issue:
        suppl_part = issue.split("Suppl.")[1].split()[0]
        suppl = int(suppl_part) if suppl_part.isdigit() else None
    
    return number, suppl