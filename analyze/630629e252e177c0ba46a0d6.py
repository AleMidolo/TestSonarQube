def retrieve_diaspora_host_meta(host):
    """
    检索远程 Diaspora 的 host-meta 文档。

    :arg host: 要检索的主机 
    :returns: ``XRD`` 实例
    """
    import requests
    from xrd import XRD
    
    # 构建 host-meta URL
    host_meta_url = f"https://{host}/.well-known/host-meta"
    
    try:
        # 发送 GET 请求获取 host-meta 文档
        response = requests.get(host_meta_url)
        response.raise_for_status()
        
        # 解析 XRD 文档
        xrd = XRD.parse_xrd(response.text)
        return xrd
        
    except requests.exceptions.RequestException as e:
        # 如果 HTTPS 失败,尝试 HTTP
        try:
            host_meta_url = f"http://{host}/.well-known/host-meta"
            response = requests.get(host_meta_url)
            response.raise_for_status()
            
            xrd = XRD.parse_xrd(response.text)
            return xrd
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to retrieve host-meta from {host}: {str(e)}")
            
    except Exception as e:
        raise Exception(f"Failed to parse host-meta from {host}: {str(e)}")