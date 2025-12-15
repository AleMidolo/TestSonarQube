class EncryptionUtils: 
    def __init__(self, key):
        """
        Initializes the class with a key.
        :param key: The key to use for encryption, str.
        """
        self.key = key

    def caesar_cipher(self, plaintext, shift):
        """
        Encrypts the plaintext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param shift: The number of characters to shift each character in the plaintext, int.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.caesar_cipher("abc", 1)
        'bcd'
        """
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                if char.isupper():
                    ascii_offset = 65
                else:
                    ascii_offset = 97
                shifted_char = chr(
                    (ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                ciphertext += shifted_char
            else:
                ciphertext += char
        return ciphertext
    
    def vigenere_cipher(self, plaintext):
        """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
        """
        encrypted_text = ""
        key_index = 0
        for char in plaintext:
            if char.isalpha():
                shift = ord(self.key[key_index % len(self.key)].lower()) - ord('a')
                encrypted_char = chr(
                    (ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
                encrypted_text += encrypted_char.upper() if char.isupper() else encrypted_char
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text
    
    def rail_fence_cipher(self, plain_text, rails):
        """
        Cripta il testo in chiaro utilizzando il cifrario Rail Fence.
        :param plain_text: Il testo in chiaro da criptare, str.
        :return: Il testo cifrato, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'
        """
        rail = [['\n' for i in range(len(plain_text))]
                for j in range(rails)]
        dir_down = None
        row, col = 0, 0

        for char in plain_text:
            if row == 0:
                dir_down = True
            if row == rails - 1:
                dir_down = False

            rail[row][col] = char
            col += 1

            if dir_down:
                row += 1
            else:
                row -= 1

        result = []
        for i in range(rails):
            for j in range(len(plain_text)):
                if rail[i][j] != '\n':
                    result.append(rail[i][j])
        return "".join(result)