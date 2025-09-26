class DecryptionUtils:
    def __init__(self, key):
        self.key = key
    
    def caesar_decipher(self, ciphertext, shift):
        return ''.join(self._caesar_decipher_char(char, shift) for char in ciphertext)
    
    def _caesar_decipher_char(self, char, shift):
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            return chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        return char
    
    def vigenere_decipher(self, ciphertext):
        decrypted_text = ""
        key_index = 0
        for char in ciphertext:
            if char.isalpha():
                shift = self._get_vigenere_shift(key_index)
                decrypted_char = self._vigenere_decrypt_char(char, shift)
                decrypted_text += decrypted_char
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text
    
    def _get_vigenere_shift(self, key_index):
        return ord(self.key[key_index % len(self.key)].lower()) - ord('a')
    
    def _vigenere_decrypt_char(self, char, shift):
        decrypted_char = chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
        return decrypted_char.upper() if char.isupper() else decrypted_char
    
    def rail_fence_decipher(self, encrypted_text, rails):
        fence = self._create_fence(encrypted_text, rails)
        self._fill_fence(fence, encrypted_text)
        return self._read_fence(fence, rails, len(encrypted_text))
    
    def _create_fence(self, encrypted_text, rails):
        return [['\n' for _ in range(len(encrypted_text))] for _ in range(rails)]
    
    def _fill_fence(self, fence, encrypted_text):
        direction = -1
        row, col = 0, 0
        for _ in range(len(encrypted_text)):
            if row == 0 or row == len(fence) - 1:
                direction = -direction
            fence[row][col] = ''
            col += 1
            row += direction

        index = 0
        for i in range(len(fence)):
            for j in range(len(encrypted_text)):
                if fence[i][j] == '':
                    fence[i][j] = encrypted_text[index]
                    index += 1
    
    def _read_fence(self, fence, rails, text_length):
        plain_text = ''
        direction = -1
        row, col = 0, 0
        for _ in range(text_length):
            if row == 0 or row == rails - 1:
                direction = -direction
            plain_text += fence[row][col]
            col += 1
            row += direction
        return plain_text