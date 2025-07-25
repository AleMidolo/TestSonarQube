def verify_relayable_signature(public_key, doc, signature):
    """
    验证已签名的XML元素，以确保声明的作者确实生成了此消息。

    :param public_key: 公钥，用于验证签名
    :param doc: 已签名的XML文档
    :param signature: 签名
    :return: 如果签名验证成功返回True，否则返回False
    """
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.backends import default_backend
    from lxml import etree

    # 加载公钥
    public_key = serialization.load_pem_public_key(
        public_key.encode(),
        backend=default_backend()
    )

    # 解析XML文档
    root = etree.fromstring(doc)

    # 获取签名内容
    signed_info = root.find(".//SignedInfo", namespaces=root.nsmap)
    if signed_info is None:
        return False

    # 计算签名内容的哈希值
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(etree.tostring(signed_info))
    hashed_data = digest.finalize()

    # 验证签名
    try:
        public_key.verify(
            signature,
            hashed_data,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        return False