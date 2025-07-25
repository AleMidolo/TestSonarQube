from typing import Dict, Any
import json
import xml.etree.ElementTree as ET

RequestType = Dict[str, Any]
Magic_ENV_TAG = "Magic_ENV_TAG"

def identify_request(request: RequestType) -> bool:
    """
    检查通过 JSON 加载的请求体是否包含事件。如果包含，则返回真；否则，检查从请求体加载的 XML 的标签是否为 Magic_ENV_TAG，如果是，则返回真。如果上述条件均不满足，则返回假。

    尝试识别这是否是一个 Diaspora 请求。

    首先尝试检查是否为公共消息，然后检查是否为私有消息。最后检查这是否是旧式（Legacy）负载。
    """
    # 检查是否为 JSON 格式并包含事件
    try:
        if isinstance(request, dict) and 'event' in request:
            return True
    except:
        pass

    # 检查是否为 XML 格式并包含 Magic_ENV_TAG
    try:
        if isinstance(request, str):
            root = ET.fromstring(request)
            if root.tag == Magic_ENV_TAG:
                return True
    except:
        pass

    # 如果上述条件均不满足，则返回假
    return False