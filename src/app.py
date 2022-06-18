import sys
import os


def prime(s):
    # your code goes here
    count = 0
    s = int(s)
    for i in range(1, s+1, 1):
        if s % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))