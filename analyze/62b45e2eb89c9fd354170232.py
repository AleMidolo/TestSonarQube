def next_version(version):
    # Split version string by dots
    parts = version.split('.')
    
    # Convert to integers while preserving leading zeros
    lengths = [len(p) for p in parts]
    nums = [int(p) for p in parts]
    
    # Start from rightmost digit
    i = len(nums) - 1
    while i >= 0:
        # If current number is 9, set to 0 and continue carrying
        if nums[i] == 9:
            nums[i] = 0
            i -= 1
        else:
            # Otherwise increment and break
            nums[i] += 1
            break
            
    # If we carried through all digits, add a 1 at the start
    if i < 0:
        nums = [1] + nums
        lengths = [1] + lengths
        
    # Convert back to strings with original zero padding
    result = []
    for num, length in zip(nums, lengths):
        result.append(str(num).zfill(length))
        
    return '.'.join(result)