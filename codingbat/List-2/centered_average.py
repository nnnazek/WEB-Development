def centered_average(nums):
    total = 0
    centered = nums
    centered.remove(max(nums))
    centered.remove(min(nums))
    for i in centered:
        total += i
    return total/len(centered)