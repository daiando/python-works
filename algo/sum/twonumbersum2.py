def twoNumberSum(array, targetSum):
    a1 = array
	ret = list()

    for x in a1:
        if a1.count(targetSum - x) != 0 and x != targetSum - x:
            ret += [ x ]

	return ret



        a1 = array
        a2 = array
    	ret = list()

        for x in a1:
            if a1.count(targetSum - x) != 0 and x != targetSum - x:
                ret += [ x ]

    	return ret
