def quicksort(input):
    l = len(input)
    if l <= 1:
        return input
    a = input[int(l/2)]
    left = []
    centre = []
    right = []
    for e in input:
        if e < a:
            left.append(e)
        elif e == a:
            centre.append(e)
        else:
            right.append(e)
    return quicksort(left) + centre + quicksort(right)

def quicksort_withshuffle(input):
    import random
    return quicksort(random.shuffle(input))



if __name__ == "__main__":
    from sys import argv
    input = []
    nos = int(argv[1])
    for i in range(0,nos):
        input.append(float(raw_input()))
    quicksort(input)

"""
Working Time for floats:
10         -  0.0153160095215 s
100        -  0.0158460140228 s
1000       -  0.0201411247253 s
10000      -  0.0705790519714 s
100000     -  0.628607034683 s
1000000    -  8.05927991867 s
"""