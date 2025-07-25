def identify_request(request: RequestType) -> bool:
    """
    检查通过 JSON 加载的请求体是否包含事件。如果包含，则返回真。否则，返回假。

    尝试识别这是否是一个 Matrix 请求。
    """
    if not request or not isinstance(request, dict):
        return False
    
    # 检查请求体中是否包含 'event' 键
    if 'event' in request:
        return True
    
    # 检查是否是 Matrix 请求
    if 'type' in request and request.get('type', '').startswith('m.'):
        return True
    
    return False