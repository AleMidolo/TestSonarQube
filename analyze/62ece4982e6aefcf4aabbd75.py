import subprocess

def addignored(ignored):
    """
    Use the git command to obtain the file names, turn it into a list, sort the list for only ignored files, return those files as a single string with each filename separated by a comma.
    """
    # Get the list of ignored files from git
    result = subprocess.run(['git', 'ls-files', '--others', '--ignored', '--exclude-standard'], capture_output=True, text=True)
    ignored_files = result.stdout.splitlines()
    
    # Filter the list to only include files that are in the ignored list
    filtered_files = [file for file in ignored_files if file in ignored]
    
    # Sort the list of ignored files
    filtered_files.sort()
    
    # Return the sorted list as a comma-separated string
    return ','.join(filtered_files)