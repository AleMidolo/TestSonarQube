def strip_root(path, root):
    """
    पथ से रूट को हटाएं, और यदि यह विफल होता है, तो अपवाद फेंकें।
    
    :param path: पथ जिससे रूट को हटाना है।
    :param root: रूट जिसे पथ से हटाना है।
    :return: रूट हटाए गए पथ।
    :raises ValueError: यदि पथ रूट से शुरू नहीं होता है।
    """
    if not path.startswith(root):
        raise ValueError(f"पथ '{path}' रूट '{root}' से शुरू नहीं होता है।")
    return path[len(root):]