def caesar_decipher(self, ciphertext, shift):
    """
    सीज़र साइफ़र का इस्तेमाल करके दिए गए साइफ़रटेक्स्ट को डिक्रिप्ट करता है।

    :param ciphertext: डिक्रिप्ट करने के लिए साइफ़रटेक्स्ट, str
    :param shift: डिक्रिप्शन के लिए इस्तेमाल होने वाला shift, int
    :return: डिक्रिप्ट किया गया प्लेनटेक्स्ट, str

    >>> d = DecryptionUtils('key')
    >>> d.caesar_decipher('ifmmp', 1)
    'hello'
    """
    plaintext = ''
    
    for char in ciphertext:
        if char.isalpha():
            # Check if uppercase or lowercase
            if char.isupper():
                # Decrypt uppercase letter
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                # Decrypt lowercase letter
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            plaintext += decrypted_char
        else:
            # Non-alphabetic characters remain unchanged
            plaintext += char
    
    return plaintext