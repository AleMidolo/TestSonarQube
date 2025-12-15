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
    
    def rail_fence_cipher(self, plain_text, rails):
        """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'
        """
        fence = [['\n' for _ in range(len(plain_text))] for _ in range(rails)]
        direction = -1
        row, col = 0, 0
    
        for char in plain_text:
            if row == 0 or row == rails-1:
                direction = -direction
    
            fence[row][col] = char
            col += 1
            row += direction
    
        encrypted_text = ''
        for i in range(rails):
            for j in range(len(plain_text)):
                if fence[i][j] != '\n':
                    encrypted_text += fence[i][j]
    
        return encrypted_text
    
    def vigenere_cipher(self, plaintext):
        """
        प्लेनटेक्स्ट को विजेनेरे सिफर का उपयोग करके एन्क्रिप्ट करता है।
        :param plaintext: एन्क्रिप्ट करने के लिए प्लेनटेक्स्ट, str.
        :return: ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
        """
        key = self.key
        key_length = len(key)
        plaintext_length = len(plaintext)
        ciphertext = ""

        for i in range(plaintext_length):
            if plaintext[i].isalpha():
                shift = ord(key[i % key_length].lower()) - ord('a')
                if plaintext[i].isupper():
                    ciphertext += chr((ord(plaintext[i]) - ord('A') + shift) % 26 + ord('A'))
                else:
                    ciphertext += chr((ord(plaintext[i]) - ord('a') + shift) % 26 + ord('a'))
            else:
                ciphertext += plaintext[i]

        return ciphertext