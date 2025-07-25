def get_versions():
    """
    संस्करण जानकारी प्राप्त करें या यदि ऐसा करने में असमर्थ हैं तो डिफ़ॉल्ट मान लौटाएं।
    """
    try:
        import pkg_resources
        versions = {pkg.project_name: pkg.version for pkg in pkg_resources.working_set}
        return versions
    except Exception:
        return {"default": "unknown"}