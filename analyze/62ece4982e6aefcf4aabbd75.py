def addignored(ignored):
    # Import subprocess to run git commands
    import subprocess
    
    # Run git ls-files command to get all files
    git_cmd = "git ls-files --others --ignored --exclude-standard"
    result = subprocess.run(git_cmd.split(), capture_output=True, text=True)
    
    # Convert output to list of filenames
    files = result.stdout.strip().split('\n')
    
    # Filter only ignored files
    ignored_files = [f for f in files if f]
    
    # Join filenames with commas
    ignored_str = ','.join(ignored_files)
    
    return ignored_str