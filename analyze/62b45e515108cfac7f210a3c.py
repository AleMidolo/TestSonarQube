def initialize(self):
    """
    创建并初始化一个新的 OCFL 存储根目录。
    """
    import os

    # Define the root directory for OCFL storage
    root_directory = "ocfl_root"

    # Check if the directory already exists
    if not os.path.exists(root_directory):
        # Create the root directory
        os.makedirs(root_directory)
        print(f"OCFL storage root directory '{root_directory}' created.")
    else:
        print(f"OCFL storage root directory '{root_directory}' already exists.")