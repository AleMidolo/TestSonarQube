def _extract_number_and_supplment_from_issue_element(issue):
    """
    समस्या (issue) की सामग्री से number और suppl के संभावित मानों को निकालें।
    
    Args:
        issue (str): समस्या की सामग्री जिसमें number और suppl के मान हो सकते हैं।
    
    Returns:
        tuple: (number, suppl) के रूप में एक tuple जहां number और suppl संभावित मान हो सकते हैं।
              यदि कोई मान नहीं मिलता है, तो None लौटाया जाएगा।
    """
    number = None
    suppl = None
    
    # यहां आप issue से number और suppl को निकालने के लिए अपना तर्क लिखें
    # उदाहरण के लिए, यदि issue में "Vol. 5, Suppl. 2" है, तो:
    # number = 5
    # suppl = 2
    
    # यह एक सरल उदाहरण है, आप इसे अपनी आवश्यकताओं के अनुसार संशोधित कर सकते हैं
    if "Vol." in issue:
        number_part = issue.split("Vol.")[1].split(",")[0].strip()
        number = int(number_part) if number_part.isdigit() else None
    
    if "Suppl." in issue:
        suppl_part = issue.split("Suppl.")[1].strip()
        suppl = int(suppl_part) if suppl_part.isdigit() else None
    
    return number, suppl