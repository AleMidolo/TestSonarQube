def verify_relayable_signature(public_key, doc, signature):
    """
    验证已签名的XML元素，以确保声明的作者确实生成了此消息。
    """
    try:
        # 导入所需的加密库
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import padding
        from cryptography.exceptions import InvalidSignature
        
        # 将XML文档转换为规范化的字节字符串
        canonical_doc = doc.encode('utf-8')
        
        # 验证签名
        try:
            public_key.verify(
                signature,
                canonical_doc,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False
            
    except Exception as e:
        # 如果验证过程中出现任何错误，返回False
        return False