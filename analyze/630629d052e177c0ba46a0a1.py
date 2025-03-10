import xml.etree.ElementTree as ET
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def verify_relayable_signature(public_key, doc, signature):
    """
    验证已签名的XML元素，以确保声明的作者确实生成了此消息。

    :param public_key: 公钥，用于验证签名
    :param doc: 要验证的XML文档
    :param signature: 签名
    :return: True如果签名验证成功，否则False
    """
    try:
        # 将XML文档转换为字符串
        doc_str = ET.tostring(doc, encoding='unicode')
        
        # 将公钥从PEM格式加载
        pub_key = serialization.load_pem_public_key(public_key.encode())
        
        # 验证签名
        pub_key.verify(
            signature,
            doc_str.encode(),
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