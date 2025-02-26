import os

def is_gitbash():
    """
    यदि आप Windows के Gitbash में प्रोग्राम चला रहे हैं तो True रिटर्न करता है।

    :return: यदि Gitbash है तो True
    """
    return os.environ.get('TERM', '').startswith('bash') and os.path.basename(os.environ.get('SHELL', '')) == 'bash'