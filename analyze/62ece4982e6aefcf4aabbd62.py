def _replace_url_args(url, url_args):
    """
    将 `url` 中的值替换为 `url_args` 中的值  
      如果 `url_args` 有值，则遍历 `url_args` 中的键和值。  
      然后用值替换 `url` 中第一个参数的键。  
      返回值：修改后的 `url`。

    将任何自定义字符串 URL 项目替换为 `args` 中的值。
    """
    for key, value in url_args.items():
        url = url.replace(f'{{{key}}}', str(value))
    return url