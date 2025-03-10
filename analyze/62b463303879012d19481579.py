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
    # उदाहरण के लिए, यदि issue में "संख्या: 123, सप्लीमेंट: ABC" है, तो:
    # number = 123
    # suppl = "ABC"
    
    # यह एक उदाहरण है, आप इसे अपने आवश्यकतानुसार संशोधित कर सकते हैं
    if "संख्या:" in issue and "सप्लीमेंट:" in issue:
        parts = issue.split(",")
        for part in parts:
            if "संख्या:" in part:
                number = int(part.split(":")[1].strip())
            elif "सप्लीमेंट:" in part:
                suppl = part.split(":")[1].strip()
    
    return (number, suppl)