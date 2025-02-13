def find_path_type(path):
    import os

    if not os.path.exists(path):
        return "Path does not exist"

    if os.path.isdir(path):
        if os.path.isfile(os.path.join(path, "0=metadata.json")):
            return "object"
        elif os.path.isfile(os.path.join(path, "0=inventory.json")):
            return "file"
        elif os.path.isfile(os.path.join(path, "0=storage.json")):
            return "root"
        else:
            return "Directory does not contain valid Namaste files"
    elif os.path.isfile(path):
        return "file"
    else:
        return "Invalid path type"