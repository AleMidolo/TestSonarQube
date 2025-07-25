def _inline_r_setup(code: str) -> str:
    # Set up R options that need to be configured after R starts
    r_setup = """
    options(warn=-1)  # Suppress warnings
    options(width=10000)  # Prevent line wrapping
    options(show.error.messages=TRUE)  # Show error messages
    options(error=function() {traceback(3); quit(status=1)})  # Exit on error with traceback
    """
    
    # Combine setup code with user code
    full_code = r_setup + "\n" + code
    
    return full_code