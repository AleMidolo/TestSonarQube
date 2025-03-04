def _inline_r_setup(code: str) -> str:
    # Define R setup options that need to be prepended to the code
    r_setup = """
options(warn=-1)  # Suppress warnings
options(width=10000)  # Prevent line wrapping
options(encoding='UTF-8')  # Set UTF-8 encoding
"""
    
    # Combine setup options with provided code
    return r_setup + "\n" + code