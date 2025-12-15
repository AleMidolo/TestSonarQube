class DecryptionUtils: 
    def __init__(self, key):
        """
        Initializes the decryption utility with a key.
        :param key: The key to use for decryption,str.
        """
        self.key = key

    def vigenere_decipher(self, ciphertext):
        """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'
        """
        decrypted_text = ""
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                shift = ord(self.key[key_index % len(self.key)].lower()) - ord('a')
                decrypted_char = chr(
                    (ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
                decrypted_text += decrypted_char.upper() if char.isupper() else decrypted_char
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text
    
    def rail_fence_decipher(self, encrypted_text, rails):
        """
        Deciphers the given ciphertext using the Rail Fence cipher
        :param encrypted_text: The ciphertext to decipher,str.
        :param rails: The number of rails to use for decryption,int.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.rail_fence_decipher('Hoo!el,Wrdl l', 3)
        'Hello, World!'
        """
        fence = [['\n' for _ in range(len(encrypted_text))] for _ in range(rails)]
        direction = -1
        row, col = 0, 0
    
        for _ in range(len(encrypted_text)):
            if row == 0 or row == rails - 1:
                direction = -direction
    
            fence[row][col] = ''
            col += 1
            row += direction
    
        index = 0
        for i in range(rails):
            for j in range(len(encrypted_text)):
                if fence[i][j] == '':
                    fence[i][j] = encrypted_text[index]
                    index += 1
    
        plain_text = ''
        direction = -1
        row, col = 0, 0
        for _ in range(len(encrypted_text)):
            if row == 0 or row == rails - 1:
                direction = -direction
    
            plain_text += fence[row][col]
            col += 1
            row += direction
    
        return plain_text
    
    def caesar_decipher(self, ciphertext, shift):
        """
        使用凯撒密码解密给定的密文
        :param ciphertext: 要解密的密文，str。
        :param shift: 用于解密的位移，int。
        :return: 解密后的明文，str。
        >>> d = DecryptionUtils('key')
        >>> d.caesar_decipher('ifmmp', 1)
        'hello'
        """
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha():
                shift_amount = shift % 26
                if char.islower():
                    decrypted_char = chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
                else:
                    decrypted_char = chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        return decrypted_text