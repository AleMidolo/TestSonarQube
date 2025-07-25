def next_version(version):
    # Split version into parts
    parts = version.split('.')
    
    # Convert to integers
    nums = [int(x) for x in parts]
    
    # Start from rightmost digit
    i = len(nums) - 1
    
    while i >= 0:
        # If current digit is 9, set to 0 and continue left
        if nums[i] == 9:
            nums[i] = 0
            i -= 1
        # Otherwise increment current digit and break
        else:
            nums[i] += 1
            break
            
    # If we ran out of digits to increment, add new digit
    if i < 0:
        nums = [1] + nums
        
    # Convert back to strings preserving leading zeros
    result = []
    for i, num in enumerate(nums):
        # Keep leading zeros if original had them
        if parts[i].startswith('0') and num != 0:
            result.append('0' + str(num))
        else:
            result.append(str(num))
            
    return '.'.join(result)