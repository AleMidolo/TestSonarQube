def vigenere_cipher(self, plaintext):
        """
        使用维吉尼亚密码加密明文。
        :param plaintext: 要加密的明文，str。
        :return: 密文，str。
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
        ciphertext = []
        key_length = len(self.key)
        key_as_int = [ord(i) - ord('a') for i in self.key.lower()]
        plaintext_int = [ord(i) - ord('a') for i in plaintext.lower()]
        
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext.append(chr(value + ord('a')))
        
        return ''.join(ciphertext)