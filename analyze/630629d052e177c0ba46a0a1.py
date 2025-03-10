from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def verify_relayable_signature(public_key, doc, signature):
    """
    验证已签名的XML元素，以确保声明的作者确实生成了此消息。

    :param public_key: 公钥，用于验证签名
    :param doc: 需要验证的XML文档（字节串）
    :param signature: 签名（字节串）
    :return: 布尔值，表示签名是否有效
    """
    try:
        # 加载公钥
        pub_key = serialization.load_pem_public_key(
            public_key,
            backend=default_backend()
        )
        
        # 验证签名
        pub_key.verify(
            signature,
            doc,
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