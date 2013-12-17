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

from sys import argv

if __name__ == "__main__":
    input = []
    nos = int(argv[1])
    for i in range(0,nos):
        input.append(float(raw_input()))
    merge_sort(input)
#print merge_sort([5,7,2,0,12,3,4])

"""
Working Time for floats:
100      - 0m0.021s
1000     - 0m0.030s
10000    - 0m0.094s
100000   - 0m0.857s
1000000  - 0m10.525s
10000000 - ?m??.???s
"""