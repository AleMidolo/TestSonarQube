def _inline_r_setup(code: str) -> str:
    # Add R options configuration commands before the user's code
    r_setup = """
options(warn=-1)  # Suppress warnings
options(width=10000)  # Prevent line wrapping in output
options(encoding='UTF-8')  # Set encoding
"""
    # Combine setup code with user code
    return r_setup + "\n" + code