from typing import Dict, Any
import json
import xml.etree.ElementTree as ET

def identify_request(request: Dict[str, Any]) -> bool:
    """
    检查通过 JSON 加载的请求体是否包含事件。如果包含，则返回真；否则，检查从请求体加载的 XML 的标签是否为 Magic_ENV_TAG，如果是，则返回真。如果上述条件均不满足，则返回假。

    尝试识别这是否是一个 Diaspora 请求。

    首先尝试检查是否为公共消息，然后检查是否为私有消息。最后检查这是否是旧式（Legacy）负载。
    """
    # 检查是否为 JSON 格式的请求体
    if 'event' in request:
        return True
    
    # 如果不是 JSON，尝试解析为 XML
    try:
        xml_data = request.get('xml', '')
        if not xml_data:
            return False
        
        root = ET.fromstring(xml_data)
        if root.tag == 'Magic_ENV_TAG':
            return True
    except ET.ParseError:
        pass
    
    # 检查是否为公共消息
    if 'public_message' in request:
        return True
    
    # 检查是否为私有消息
    if 'private_message' in request:
        return True
    
    # 检查是否为旧式（Legacy）负载
    if 'legacy_payload' in request:
        return True
    
    # 如果以上条件都不满足，返回 False
    return False