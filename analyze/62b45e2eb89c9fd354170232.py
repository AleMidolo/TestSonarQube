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
    for i in range(len(nums)-1, -1, -1):
        nums[i] += 1
        # If no carry needed, we're done
        if nums[i] < 10 ** lengths[i]:
            break
        # Carry to next digit
        nums[i] = 0
        # If we're at leftmost digit, extend length
        if i == 0:
            lengths[i] += 1
            
    # Convert back to strings with original zero padding
    result = []
    for num, length in zip(nums, lengths):
        result.append(str(num).zfill(length))
        
    return '.'.join(result)