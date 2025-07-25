def next_version(version):
    """
    Next version identifier following existing pattern.
    
    Must deal with both zero-prefixed and non-zero prefixed versions.
    """
    # Split version string into parts
    parts = version.split('.')
    
    # Convert to integers while preserving leading zeros
    lengths = [len(p) for p in parts]
    nums = [int(p) for p in parts]
    
    # Start from rightmost digit and increment
    i = len(nums) - 1
    while i >= 0:
        nums[i] += 1
        if nums[i] < 10 ** lengths[i]:  # No overflow
            break
        nums[i] = 0
        i -= 1
        
    # Convert back to strings with original zero padding
    result = []
    for num, length in zip(nums, lengths):
        result.append(str(num).zfill(length))
        
    return '.'.join(result)