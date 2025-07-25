def find_path_type(path):
    import os
    import glob

    # Check if path exists
    if not os.path.exists(path):
        return "Error: Path does not exist"

    # Check if it's a directory
    if not os.path.isdir(path):
        if os.path.isfile(path):
            return "file"
        return "Error: Path is neither file nor directory"

    # Look for Namaste files starting with "0="
    namaste_files = glob.glob(os.path.join(path, "0=*"))
    
    if not namaste_files:
        return "Error: No Namaste files found"

    # Read first Namaste file content
    try:
        with open(namaste_files[0], 'r') as f:
            content = f.read().strip()
            
        # Check content for OCFL root
        if content.startswith("ocfl_"):
            return "root"
            
        # Check content for OCFL object
        elif content.startswith("ocfl_object_"):
            return "object"
            
    except Exception as e:
        return f"Error reading Namaste file: {str(e)}"
        
    return "Error: Unknown Namaste file content"