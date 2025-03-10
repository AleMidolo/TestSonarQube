from typing import Dict, Any

def identify_request(request: Dict[str, Any]) -> bool:
    """
    检查通过 JSON 加载的请求体是否包含事件。如果包含，则返回真。否则，返回假。

    尝试识别这是否是一个 Matrix 请求。
    """
    # 检查请求体中是否包含 'event' 键
    if 'event' in request:
        return True
    return False