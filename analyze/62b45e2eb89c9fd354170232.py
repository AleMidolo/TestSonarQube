def next_version(version):
    # Split version string into parts
    parts = version.split('.')
    
    # Convert parts to integers
    nums = [int(x) for x in parts]
    
    # Start from rightmost digit
    i = len(nums) - 1
    
    while i >= 0:
        # If current digit is less than 9, increment it and break
        if nums[i] < 9:
            nums[i] += 1
            break
        # If current digit is 9, set to 0 and continue to next digit
        nums[i] = 0
        i -= 1
        
    # If we've gone through all digits and they're all 9s
    # Add a new digit 1 at the start
    if i < 0:
        nums.insert(0, 1)
    
    # Convert back to strings preserving original zero padding
    result = []
    for i in range(len(parts)):
        # Get original length of this part
        orig_len = len(parts[i])
        # Format number with same number of digits
        result.append(str(nums[i]).zfill(orig_len))
        
    return '.'.join(result)