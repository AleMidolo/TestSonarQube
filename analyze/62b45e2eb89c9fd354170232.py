def next_version(version):
    # Split version string into parts
    parts = version.split('.')
    
    # Convert parts to integers
    nums = [int(x) for x in parts]
    
    # Start from rightmost digit
    i = len(nums) - 1
    
    while i >= 0:
        # If current digit is 9, set to 0 and continue to next digit
        if nums[i] == 9:
            nums[i] = 0
            i -= 1
        # Otherwise increment current digit and break
        else:
            nums[i] += 1
            break
    
    # If we ran out of digits to increment, add a 1 at the start
    if i < 0:
        nums = [1] + nums
        
    # Convert back to strings, preserving any leading zeros
    result = []
    for i, num in enumerate(nums):
        # Get original length of this part
        orig_len = len(parts[i]) if i < len(parts) else 1
        # Format with leading zeros if needed
        result.append(str(num).zfill(orig_len))
        
    return '.'.join(result)