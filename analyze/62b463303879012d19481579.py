def _extract_number_and_supplment_from_issue_element(issue):
    """
    从 issue 的内容中返回 number 和 sup 的可能值。
    从 issue 的内容中提取 number 和 suppl 的可能值。
    """
    # 初始化返回值
    number = None
    suppl = None
    
    # 如果 issue 为空则直接返回
    if not issue:
        return number, suppl
        
    # 移除空白字符
    issue = issue.strip()
    
    # 处理常见的补充格式,如 "1 suppl", "1 s", "1s"等
    if "suppl" in issue.lower() or "s" in issue.lower():
        parts = issue.lower().replace("suppl", "s").split()
        if len(parts) >= 2:
            try:
                number = int(parts[0])
                suppl = "s"
            except ValueError:
                pass
        elif len(parts) == 1 and parts[0].endswith("s"):
            try:
                number = int(parts[0][:-1])
                suppl = "s"
            except ValueError:
                pass
    # 处理纯数字的情况
    else:
        try:
            number = int(issue)
        except ValueError:
            pass
            
    return number, suppl