def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
        """
        ciphertext = ""
        key_length = len(self.key)
        key_as_int = [ord(i) - ord('a') for i in self.key.lower()]
        plaintext_int = [ord(i) - ord('a') for i in plaintext.lower()]
        
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
            ciphertext += chr(value + ord('a'))
        
        return ciphertext