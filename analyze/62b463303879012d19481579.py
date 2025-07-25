def _extract_number_and_supplment_from_issue_element(issue):
    """
    从 issue 的内容中返回 number 和 sup 的可能值。
    从 issue 的内容中提取 number 和 suppl 的可能值。
    """
    number = None
    suppl = None
    
    # 假设 issue 是一个字符串，包含数字和可能的补充信息
    # 例如: "123 Suppl 2" 或 "456"
    parts = issue.split()
    
    if parts:
        # 提取 number
        if parts[0].isdigit():
            number = int(parts[0])
        
        # 提取 suppl
        if len(parts) > 1 and parts[1].lower() == "suppl" and len(parts) > 2 and parts[2].isdigit():
            suppl = int(parts[2])
    
    return number, suppl