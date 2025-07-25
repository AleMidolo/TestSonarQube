import re

def _extract_number_and_supplment_from_issue_element(issue):
    """
    从 issue 的内容中返回 number 和 sup 的可能值。
    从 issue 的内容中提取 number 和 suppl 的可能值。
    """
    # 假设 issue 是一个字符串，包含数字和可能的补充信息
    # 使用正则表达式提取数字和补充信息
    number_match = re.search(r'\d+', issue)
    suppl_match = re.search(r'suppl\.?\s*(\d+)', issue, re.IGNORECASE)
    
    number = number_match.group(0) if number_match else None
    suppl = suppl_match.group(1) if suppl_match else None
    
    return number, suppl