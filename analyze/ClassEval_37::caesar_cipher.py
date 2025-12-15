class EncryptionUtils: 
    def __init__(self, key):
        """
        Initializes the class with a key.
        :param key: The key to use for encryption, str.
        """
        self.key = key

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
    
    def rail_fence_cipher(self, plaintext, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'
        """
        fence = [['\n' for _ in range(len(plaintext))] for _ in range(rails)]
        direction = -1
        row, col = 0, 0
    
        for char in plaintext:
            if row == 0 or row == rails-1:
                direction = -direction
    
            fence[row][col] = char
            col += 1
            row += direction
    
        encrypted_text = ''
        for i in range(rails):
            for j in range(len(plaintext)):
                if fence[i][j] != '\n':
                    encrypted_text += fence[i][j]
    
        return encrypted_text
    
    def caesar_cipher(self, plaintext, shift):
        """
        Encrypts the plaintext using the Caesar cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param shift: The number of positions to shift each character in the plaintext, int.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.caesar_cipher("abc", 1)
        'bcd'
        """
        encrypted_text = ""
        for char in plaintext:
            if char.isalpha():
                shift_amount = shift % 26
                if char.islower():
                    encrypted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
                else:
                    encrypted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text