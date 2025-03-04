def find_path_type(path):
    import os
    
    # Check if path exists
    if not os.path.exists(path):
        return "Path does not exist"
        
    # If it's a file, return 'file'
    if os.path.isfile(path):
        return "file"
        
    # If it's not a directory, return error
    if not os.path.isdir(path):
        return "Path is neither file nor directory"
        
    # Look for namaste files in directory
    files = os.listdir(path)
    namaste_files = [f for f in files if f.startswith("0=")]
    
    if not namaste_files:
        return "No namaste files found"
        
    # Check content of first namaste file
    namaste_path = os.path.join(path, namaste_files[0])
    try:
        with open(namaste_path) as f:
            content = f.read().strip()
            
        if content == "ocfl_object_1.0":
            return "object"
        elif content == "ocfl_1.0":
            return "root"
        else:
            return f"Unknown namaste file content: {content}"
            
    except Exception as e:
        return f"Error reading namaste file: {str(e)}"