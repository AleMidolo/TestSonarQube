def next_version(version):
    # Split version into parts by dots
    parts = version.split('.')
    
    # Convert parts to integers and increment last number
    nums = [int(x) for x in parts]
    
    # Start from rightmost digit
    i = len(nums) - 1
    while i >= 0:
        # Increment current digit
        nums[i] += 1
        
        # If no overflow, we're done
        if nums[i] < 10:
            break
            
        # Handle overflow
        nums[i] = 0
        i -= 1
        
        # Handle overflow in leftmost position
        if i < 0:
            nums.insert(0, 1)
            
    # Convert back to strings preserving leading zeros
    result = []
    for i, num in enumerate(nums):
        # Get original length of this part
        orig_len = len(parts[i]) if i < len(parts) else 1
        # Format with leading zeros if needed
        result.append(str(num).zfill(orig_len))
        
    return '.'.join(result)