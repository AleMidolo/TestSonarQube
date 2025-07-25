def _inline_r_setup(code: str) -> str:
    # Add R options setup code before the user's code
    setup_code = """
options(warn=-1)  # Suppress warnings
options(width=120)  # Set output width
options(scipen=999)  # Avoid scientific notation
options(stringsAsFactors=FALSE)  # Don't convert strings to factors by default
"""
    
    # Combine setup code with user code
    full_code = setup_code + "\n" + code
    
    return full_code