def addignored(ignored):
    # Import subprocess to run git commands
    import subprocess
    
    # Run git ls-files command to get all files
    git_files = subprocess.run(['git', 'ls-files', '--ignored', '--exclude-standard'], 
                             capture_output=True, text=True)
    
    # Convert output to list, split on newlines and remove empty strings
    ignored_files = [x for x in git_files.stdout.split('\n') if x]
    
    # Filter list to only include files that match ignored pattern
    if ignored:
        ignored_files = [f for f in ignored_files if ignored in f]
        
    # Join filenames with commas
    result = ','.join(ignored_files)
    
    return result