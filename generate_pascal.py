class Solution():
    # Need to revamp code for performance improvement
    # Each node can be calculated directly e.g. 3C1 = 3/1 = 3; 3C2 = 3x2/(1x2) = 3; 4C2 = 4x3/(1x2) = 6; 5C2 = 5x4/(1x2) = 10
    def generate(self, numRows):
        pt =[]
        for i in range(numRows):
            rowvals=[]
            for j in range(i+1):
                rowvals = rowvals + [self.calcNode(i,j)]
            pt.append(rowvals)
        return pt

    def calcNode(self,k,l):
        val = 1
        for i in range(l):
            # THIS DOESN'T WORK as the division as formulated here
            # can result in non-integral answers and unfortunately
            # the computer representation of decimals suffers from 
            # rounding errors and loss of digits
            val *= (k-i)/(i+1)
        return val

def main():
    print("Debug line one")
    y = Solution()
    print(y.generate(5))

if __name__ == "__main__":
    main()
