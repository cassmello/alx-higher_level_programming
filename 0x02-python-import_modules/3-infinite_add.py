#!/usr/bin/python3



def add_arg(argv):
    g = len(argv) - 1
    if g == 0:
        print("{:d}".format(g))
        return
    else:
        x = 1
        add = 0
        while x <= g:
            add += int(argv[x])
            x += 1
        print("{:d}".format(add))


if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
