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
        if method.lower() == "post":
            response = requests.post(url, data=data, timeout=timeout, *args, **kwargs)
        else:
            raise ValueError("Unsupported method: {}".format(method))

        return response.status_code, None
    except Exception as e:
        return None, e