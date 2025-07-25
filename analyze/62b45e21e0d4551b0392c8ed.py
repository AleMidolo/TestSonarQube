def find_path_type(path):
    import os
    
    # Check if path exists
    if not os.path.exists(path):
        return "Path does not exist"
        
    # Check if it's a directory
    if not os.path.isdir(path):
        if os.path.isfile(path):
            return "file"
        return "Path is not a directory"

    # Look for Namaste files starting with "0="
    namaste_files = [f for f in os.listdir(path) if f.startswith("0=")]
    
    if not namaste_files:
        return "No Namaste files found"
        
    # Check content of first Namaste file
    namaste_content = ""
    try:
        with open(os.path.join(path, namaste_files[0]), 'r') as f:
            namaste_content = f.read().strip()
    except:
        return "Error reading Namaste file"

    # Check for OCFL Storage Root
    if "ocfl_" in namaste_content.lower():
        return "root"
        
    # Check for OCFL Object
    if "ocfl" in namaste_content.lower() and "object" in namaste_content.lower():
        return "object"
        
    return f"Unknown Namaste content: {namaste_content}"