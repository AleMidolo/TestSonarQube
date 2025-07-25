def get_nodeinfo_well_known_document(url, document_path=None):
    """
    返回一个格式化的字典，其中包括如 `url` 和 `document_path` 等信息。

    生成一个 NodeInfo 的 `.well-known` 文档。

    参考规范: http://nodeinfo.diaspora.software

    :arg url: 完整的基础 URL，包含协议，例如 `https://example.com`
    :document_path: 如果提供了自定义的 NodeInfo 文档路径，则使用该路径（可选）
    :返回值: 字典
    """
    nodeinfo = {
        "version": "2.0",
        "url": url,
    }
    
    if document_path:
        nodeinfo["document_path"] = document_path
    
    return nodeinfo