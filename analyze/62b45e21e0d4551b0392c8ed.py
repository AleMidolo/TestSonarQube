def find_path_type(path):
    import os
    import glob

    # Check if path exists
    if not os.path.exists(path):
        return "Path does not exist"

    # Look for Namaste files matching 0=*
    namaste_files = glob.glob(os.path.join(path, "0=*"))
    
    if not namaste_files:
        if os.path.isfile(path):
            return "file"
        return "No Namaste files found"

    # Read first Namaste file content
    try:
        with open(namaste_files[0], 'r') as f:
            content = f.read().strip()
            
        # Check for OCFL Storage Root
        if content.startswith("ocfl_"):
            return "root"
            
        # Check for OCFL Object
        elif content.startswith("ocfl"):
            return "object"
            
    except Exception as e:
        return f"Error reading Namaste file: {str(e)}"
        
    return "Unknown Namaste file type"