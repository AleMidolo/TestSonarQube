import xml.etree.ElementTree as ET
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def verify_relayable_signature(public_key, doc, signature):
    """
    验证已签名的XML元素，以确保声明的作者确实生成了此消息。

    :param public_key: 公钥，用于验证签名
    :param doc: 已签名的XML文档
    :param signature: 签名
    :return: 如果签名验证成功返回True，否则返回False
    """
    try:
        # 加载公钥
        pub_key = serialization.load_pem_public_key(public_key)

        # 将XML文档转换为字节
        doc_bytes = ET.tostring(doc, encoding='utf-8')

        # 验证签名
        pub_key.verify(
            signature,
            doc_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"Signature verification failed: {e}")
        return False