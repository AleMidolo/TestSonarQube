def addignored(ignored):
    """
    Use the git command to obtain the file names, turn it into a list, sort the list for only ignored files, return those files as a single string with each filename separated by a comma.
    """
    import subprocess
    
    # Run git ls-files command to get list of ignored files
    git_command = ["git", "ls-files", "--others", "--ignored", "--exclude-standard"]
    result = subprocess.run(git_command, capture_output=True, text=True)
    
    # Split output into list and remove empty strings
    ignored_files = [x for x in result.stdout.split('\n') if x]
    
    # Sort the list
    ignored_files.sort()
    
    # Join list elements with commas
    return ','.join(ignored_files)