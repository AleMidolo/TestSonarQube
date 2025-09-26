class EncryptionUtils:
    def __init__(self, key):
        self.key = key

    def caesar_cipher(self, plaintext, shift):
        return ''.join(self._shift_char(char, shift) for char in plaintext)

    def _shift_char(self, char, shift):
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            return chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        return char

    def vigenere_cipher(self, plain_text):
        encrypted_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                shift = self._get_vigenere_shift(key_index)
                encrypted_char = self._shift_vigenere_char(char, shift)
                encrypted_text += encrypted_char
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text

    def _get_vigenere_shift(self, key_index):
        return ord(self.key[key_index % len(self.key)].lower()) - ord('a')

    def _shift_vigenere_char(self, char, shift):
        encrypted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
        return encrypted_char.upper() if char.isupper() else encrypted_char

    def rail_fence_cipher(self, plain_text, rails):
        fence = [['\n' for _ in range(len(plain_text))] for _ in range(rails)]
        direction = -1
        row, col = 0, 0

        for char in plain_text:
            if row == 0 or row == rails - 1:
                direction = -direction

            fence[row][col] = char
            col += 1
            row += direction

        return self._construct_rail_fence_output(fence, rails, len(plain_text))

    def _construct_rail_fence_output(self, fence, rails, length):
        encrypted_text = ''
        for i in range(rails):
            for j in range(length):
                if fence[i][j] != '\n':
                    encrypted_text += fence[i][j]
        return encrypted_text