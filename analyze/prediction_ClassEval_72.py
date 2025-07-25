import re


class RegexUtils:

    EMAIL_PATTERN = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    PHONE_NUMBER_PATTERN = r'\b\d{3}-\d{3}-\d{4}\b'
    SPLIT_SENTENCES_PATTERN = r'[.!?][\s]{1,2}(?=[A-Z])'

    def match(self, pattern, text):
        return re.match(pattern, text) is not None

    def findall(self, pattern, text):
        return re.findall(pattern, text)

    def split(self, pattern, text):
        return re.split(pattern, text)

    def sub(self, pattern, replacement, text):
        return re.sub(pattern, replacement, text)

    def split_sentences(self, text):
        return self.split(self.SPLIT_SENTENCES_PATTERN, text)

    def validate_phone_number(self, phone_number):
        return self.match(self.PHONE_NUMBER_PATTERN, phone_number)

    def extract_email(self, text):
        return self.findall(self.EMAIL_PATTERN, text)