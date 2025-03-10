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
    
    for part in parts:
        if part.isdigit():
            number = int(part)
        elif part.lower().startswith('suppl'):
            suppl = part.split()[-1]  # 提取补充信息
    
    return number, suppl