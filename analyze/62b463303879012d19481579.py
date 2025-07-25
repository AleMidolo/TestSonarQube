def _extract_number_and_supplment_from_issue_element(issue):
    """
    从 issue 的内容中返回 number 和 sup 的可能值。
    从 issue 的内容中提取 number 和 suppl 的可能值。
    """
    number = None
    suppl = None
    
    # 假设 issue 是一个字符串，包含数字和可能的补充信息
    if isinstance(issue, str):
        # 提取数字部分
        import re
        number_match = re.search(r'\d+', issue)
        if number_match:
            number = int(number_match.group())
        
        # 提取补充信息部分
        suppl_match = re.search(r'[a-zA-Z]+', issue)
        if suppl_match:
            suppl = suppl_match.group()
    
    return number, suppl