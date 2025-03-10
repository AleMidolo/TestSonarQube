def get_spec_defaults(self):
    """
    स्पेक और अन्य स्रोतों से तर्कों के डिफ़ॉल्ट मान प्राप्त करें।
    """
    # Assuming self.spec is a dictionary or similar structure that holds the default values
    if hasattr(self, 'spec'):
        return self.spec.get('defaults', {})
    else:
        return {}