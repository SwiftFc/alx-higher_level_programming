#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = [int(arg) for arg in sys.argv[1:]]
    myresult = sum(arguments)
    print(myresult)
