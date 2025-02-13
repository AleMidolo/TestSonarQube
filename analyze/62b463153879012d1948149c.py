def select_filenames_by_prefix(prefix, files):
    import os
    return [file for file in files if os.path.basename(file).startswith(prefix)]