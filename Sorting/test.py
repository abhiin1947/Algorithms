import os
import timeit
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print "Error. Not enough arguments"
    else:
        file_to_execute = argv[1]
        i = 10
        print '"""'
        print 'Working Time for floats:'
        while i < 100000:
            os.system("rm test.txt")
            os.system("python generate_numbers.py "+str(i)+" > test.txt")
            tstr = 'os.system("python '+file_to_execute+' '+str(i)+' < test.txt")'
            #print tstr
            out = timeit.timeit(tstr,setup = "import os",number =1)
            #print "for ",i," numbers the out is:"
            print str(i),(9-len(str(i)))*" ","- ",
            print out,
            print "s"
            i *= 10
        print '"""'

"""

Example Usage - python test.py merge_sort.py

"""