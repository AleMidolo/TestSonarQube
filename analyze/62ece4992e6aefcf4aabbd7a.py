import os
import platform

def is_gitbash():
    """
    यदि आप Windows के Gitbash में प्रोग्राम चला रहे हैं तो True रिटर्न करता है।

    :return: यदि Gitbash है तो True
    """
    return platform.system() == "Windows" and "git-bash" in os.environ.get("TERM", "")