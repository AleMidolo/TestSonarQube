import json
import xml.etree.ElementTree as ET

def identify_request(request: RequestType) -> bool:
    """
    检查通过 JSON 加载的请求体是否包含事件。如果包含，则返回真；否则，检查从请求体加载的 XML 的标签是否为 Magic_ENV_TAG，如果是，则返回真。如果上述条件均不满足，则返回假。

    尝试识别这是否是一个 Diaspora 请求。

    首先尝试检查是否为公共消息，然后检查是否为私有消息。最后检查这是否是旧式（Legacy）负载。
    """
    try:
        # 尝试解析为 JSON
        data = json.loads(request.body)
        if 'event' in data:
            return True
    except json.JSONDecodeError:
        pass

    try:
        # 尝试解析为 XML
        root = ET.fromstring(request.body)
        if root.tag == 'Magic_ENV_TAG':
            return True
    except ET.ParseError:
        pass

    # 检查是否为公共消息
    if 'public_message' in request.headers:
        return True

    # 检查是否为私有消息
    if 'private_message' in request.headers:
        return True

    # 检查是否为旧式负载
    if 'legacy_payload' in request.headers:
        return True

    return False