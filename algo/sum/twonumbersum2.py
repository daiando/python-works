def twoNumberSum(array, targetSum):
    a1 = array
	ret = list()

    for x in a1:
        if a1.count(targetSum - x) != 0 and x != targetSum - x:
            ret += [ x ]

	return ret

#use dictionary

    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in array:
            return [ num, potentialMatch ]
        else:
            nums[num] = True

    return []

# O(n) time | O(n) space
