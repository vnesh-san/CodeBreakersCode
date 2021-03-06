# tc: o(n), sc: o(1)
def isValidSubsequence(array, sequence):
    if len(sequence) == 1:
        return True if sequence[0] in array else False

    if len(sequence) > len(array):
        return False
    
    p1, p2 = 0, 0

    while p1 < len(array) and p2 < len(sequence):
        if p2 == len(sequence):
            break

        if array[p1] == sequence[p2]:
            p1 += 1
            p2 += 1
        else:
            p1 += 1

    return (p2 == len(sequence)
           
# Single pointer solution
# tc: o(n), sc: o(1)
def isValidSubsequence(array, sequence):
    ptr = 0

    for i in range(len(sequence)):
        num = sequence[i]
        
        if num in array[ptr:]:
            ptr += array[ptr:].index(num) + 1
        else:
            return False

    return True
