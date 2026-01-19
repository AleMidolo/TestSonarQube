def get_mode(self):
    """
    वर्तमान कार्य मोड प्राप्त करें
    :return mode: str, कार्य मोड। केवल ['heat', 'cool']
    """
    return self.mode if hasattr(self, 'mode') and self.mode in ['heat', 'cool'] else 'cool'