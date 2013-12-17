import random
from sys import argv

limit = 100000000

if __name__ == "__main__":
    num = []
    nos = int(argv[1])
    for i in range(0,nos):
        num.append(random.random()*limit)
        print random.random()*limit