"""

"""


import sys

def debug(*values, **kwargs):
    print(*values, file=sys.stderr, **kwargs)

def debug_2d(arr, **kwargs):
    for row in arr:
        debug(row)
    debug(**kwargs)

def ii(): return int(input())
def ia(): return list(map(int, input().split()))


def main():
    pass


if __name__ == "__main__":
    main()
