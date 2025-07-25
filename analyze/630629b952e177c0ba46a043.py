def get_nodeinfo_well_known_document(url, document_path=None):
    """
    返回一个格式化的字典，其中包括如 `url` 和 `document_path` 等信息。

    生成一个 NodeInfo 的 `.well-known` 文档。

    参考规范: http://nodeinfo.diaspora.software

    :arg url: 完整的基础 URL，包含协议，例如 `https://example.com`
    :document_path: 如果提供了自定义的 NodeInfo 文档路径，则使用该路径（可选）
    :返回值: 字典
    """
    # 移除URL末尾的斜杠
    url = url.rstrip('/')
    
    # 如果没有提供document_path,使用默认路径
    if document_path is None:
        document_path = '/nodeinfo/2.0'
    else:
        # 确保document_path以/开头
        document_path = f"/{document_path.lstrip('/')}"
    
    # 构建返回的字典
    well_known_doc = {
        "links": [
            {
                "rel": "http://nodeinfo.diaspora.software/ns/schema/2.0",
                "href": f"{url}{document_path}"
            }
        ]
    }
    
    return well_known_doc