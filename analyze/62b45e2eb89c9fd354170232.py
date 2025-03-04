def next_version(version):
    # Split version string into parts
    parts = version.split('.')
    
    # Convert parts to integers and store original lengths
    orig_lengths = [len(p) for p in parts]
    nums = [int(p) for p in parts]
    
    # Start from rightmost digit and increment
    for i in range(len(nums)-1, -1, -1):
        nums[i] += 1
        if nums[i] < 10:
            break
        nums[i] = 0
        # Continue loop to increment next digit
        
    # If we overflowed the leftmost digit, add a new digit
    if nums[0] == 0:
        nums.insert(0, 1)
        orig_lengths.insert(0, 1)
        
    # Convert back to strings with original zero padding
    result = []
    for num, length in zip(nums, orig_lengths):
        result.append(str(num).zfill(length))
        
    return '.'.join(result)