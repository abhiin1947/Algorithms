import os
from sys import argv

if __name__ == "__main__":
    if len(argv) < 2:
        print "Error. Not enough arguments"
    else:
        file_to_execute = argv[1]
        i = 10
        while i < 100000000:
            os.system("rm test.txt")
            os.system("python generate_numbers.py "+str(i)+" > test.txt")
            out = os.system("time python "+file_to_execute+" "+str(i)+" < test.txt")
            print "for ",i," numbers the out is:"
            print out
            i *= 10