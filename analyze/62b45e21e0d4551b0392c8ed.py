def find_path_type(path):
    import os
    import glob

    # Check if path exists
    if not os.path.exists(path):
        return "Path does not exist"

    # If path is a file
    if os.path.isfile(path):
        return "file"

    # If path is a directory
    if os.path.isdir(path):
        # Look for namaste files matching 0=*
        namaste_files = glob.glob(os.path.join(path, "0=*"))
        
        if not namaste_files:
            return "No namaste files found"
            
        # Read first namaste file content
        try:
            with open(namaste_files[0], 'r') as f:
                content = f.read().strip()
                
            # Check content for root vs object
            if content == "ocfl_1.0":
                return "root"
            elif content == "ocfl_object_1.0":
                return "object"
            else:
                return f"Unknown namaste file content: {content}"
                
        except Exception as e:
            return f"Error reading namaste file: {str(e)}"
            
    return "Unknown path type"