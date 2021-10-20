def twoNumberSum(array, targetSum):
    a1 = array
    a2 = array
	ret = list()
	for n1 in a1:
		for n2 in a2:
			if n1 + n2 == targetSum and n1 != n2:
				ret += [ n1, n2 ]

	ret =list(set(ret))
	return ret
