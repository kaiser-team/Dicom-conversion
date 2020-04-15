import sys
import os
import logging

if __name__ == '__main__':
    path = sys.argv[1]

    print(os.listdir(path))
