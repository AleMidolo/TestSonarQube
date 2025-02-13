def was_processed(processed, path_name, verbose):
    import os

    abs_path = os.path.abspath(path_name)
    
    if abs_path in processed:
        if verbose:
            print(f"Warning: {abs_path} has already been processed.")
        return True
    else:
        processed.add(abs_path)
        return False