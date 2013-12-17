def insertion_sort(input):
    sorted_arr = []
    for e in input:
        inserted = 0
        for i in range(0,len(sorted_arr)-1):
            if e < sorted_arr[i]:
                sorted_arr.insert(i,e)
                inserted = 1
                break
        if inserted == 0:
            sorted_arr.append(e)
    return sorted_arr

def insertionsort_withshuffle(input):
    import random
    random.shuffle(input)
    return insertion_sort(input)

if __name__ == "__main__":
    from sys import argv
    input = []
    nos = int(argv[1])
    for i in range(0,nos):
        input.append(float(raw_input()))
    insertionsort_withshuffle(input)

"""
Without Shuffle
Working Time for floats:
10         -  0.017618894577 s
100        -  0.0144150257111 s
1000       -  0.0387680530548 s
10000      -  2.17563009262 s
"""

"""
With Shuffle
Working Time for floats:
10         -  0.0156950950623 s
100        -  0.015820980072 s
1000       -  0.0356900691986 s
10000      -  2.21810388565 s
"""
