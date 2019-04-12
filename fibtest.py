# Test file for calling imported library functions

from fibonacci import Solution


def main():
    y = Solution()
    x = y.fib(3)
    print(x)
    for i in range(17):
        print(y.fib(i),"=>",end="")

if __name__=="__main__":
    main()     