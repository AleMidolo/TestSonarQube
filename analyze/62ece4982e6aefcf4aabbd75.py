import subprocess

def addignored(ignored):
    """
    Use the git command to obtain the file names, turn it into a list, sort the list for only ignored files, 
    return those files as a single string with each filename separated by a comma.
    """
    # Get the list of all files in the repository
    result = subprocess.run(['git', 'ls-files', '--others', '--ignored', '--exclude-standard'], 
                            stdout=subprocess.PIPE, text=True)
    files = result.stdout.splitlines()
    
    # Filter the files that are in the ignored list
    ignored_files = [file for file in files if file in ignored]
    
    # Sort the ignored files
    ignored_files.sort()
    
    # Return the sorted ignored files as a comma-separated string
    return ', '.join(ignored_files)