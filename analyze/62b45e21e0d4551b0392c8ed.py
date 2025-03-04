def find_path_type(path):
    import os
    import glob

    # Check if path exists
    if not os.path.exists(path):
        return "Path does not exist"

    # Look for Namaste files matching 0=*
    namaste_files = glob.glob(os.path.join(path, "0=*"))

    # If no Namaste files found
    if not namaste_files:
        if os.path.isfile(path):
            return "file"
        return "No Namaste files found"

    # Read contents of first Namaste file
    try:
        with open(namaste_files[0], 'r') as f:
            content = f.read().strip()
            
        # Check content for OCFL patterns
        if "ocfl_object" in content.lower():
            return "object"
        elif "ocfl_" in content.lower():
            return "root"
        else:
            return "Unknown Namaste file content"
            
    except Exception as e:
        return f"Error reading Namaste file: {str(e)}"