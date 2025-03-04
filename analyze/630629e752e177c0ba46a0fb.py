def send_document(url, data, timeout=10, method="post", *args, **kwargs):
    """
    通过POST方法发送包含数据的响应。

    用于通过POST方法发送文档的辅助方法。

    额外的``*args``和``**kwargs``参数将会传递给``requests.post``。

    :arg url: 完整的目标URL，包括协议
    :arg data: 要在请求体中发送的数据，可以是字典（将会被表单编码）、字节数据或类似文件的对象。
    :arg timeout: 等待响应的超时时间（以秒为单位，默认为10秒）。
    :arg method: 使用的HTTP方法，默认为POST。
    :return: 返回一个元组，包含状态码（整数或None）和错误信息（异常类实例或None）。
    """
    import requests
    
    try:
        # 将method转换为小写并获取对应的请求方法
        method = method.lower()
        request_method = getattr(requests, method)
        
        # 发送请求
        response = request_method(
            url,
            data=data,
            timeout=timeout,
            *args,
            **kwargs
        )
        
        # 检查响应状态码
        response.raise_for_status()
        
        return response.status_code, None
        
    except requests.exceptions.RequestException as e:
        # 处理请求异常
        if hasattr(e.response, 'status_code'):
            return e.response.status_code, e
        return None, e
    except Exception as e:
        # 处理其他异常
        return None, e