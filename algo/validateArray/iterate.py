def isValidSubsequence(array, sequence):
    if len(array) < len(sequence):
        ret = False
    elif len(array) == len(sequence):
		if array == sequence:
            ret = True
        else:
            ret = False
    else:
        pos = 0
        next = 0
        for seq in sequence:
            if not seq in array:
                ret = False
                break
            next = array.index(seq)
            if pos >= next and sequence.index(seq) != 0:
                ret = False
                break
            else:
                ret = True
                pos = next

    return ret


    ## below is the ideal answer.

        arrIdx = 0
        seqIdx = 0
        while seqIdx < len(sequence) and arrIdx < len(array):
            if array[arrIdx] == sequence[seqIdx]:
                seqIdx += 1
            arrIdx += 1
        return seqIdx == len(sequence)
