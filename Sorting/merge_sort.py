def merge(left,right):
    i = 0
    j = 0
    new = []
    while i < len(left) and j < len(right):
        if left[i] < right [j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    if i == len(left):
        return new + right[j:]
    elif j == len(right):
        return new + left[i:]

def merge_sort(input):
    l = len(input)
    if l <= 1:
        return input
    left = input[:l/2]
    right = input[l/2:]
    return merge(merge_sort(left),merge_sort(right))


if __name__ == "__main__":
    from sys import argv
    input = []
    nos = int(argv[1])
    for i in range(0,nos):
        input.append(float(raw_input()))
    merge_sort(input)
#print merge_sort([5,7,2,0,12,3,4])

"""
Working Time for floats:
10         -  0.0142028331757 s
100        -  0.0147461891174 s
1000       -  0.0219941139221 s
10000      -  0.0828061103821 s
100000     -  0.853661060333 s
1000000    -  10.2086868286 s
"""