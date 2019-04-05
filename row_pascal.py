class Solution():
    # We need to generate a given row in Pascal's triangle
    # Each node can be calculated directly e.g. 3C1 = 3/1 = 3; 3C2 = 3x2/(1x2) = 3; 4C2 = 4x3/(1x2) = 6; 5C2 = 5x4/(1x2) = 10
    def getRow(self, rowIndex):
        rowvals=[]
        for j in range(rowIndex+1):
            rowvals = rowvals + [self.calcNode(rowIndex,j)]
        return rowvals

    def calcNode(self,k,l):
        val = 1
        for i in range(1,l+1):
            val *= (k+1-i)
            val /= i
        return int(val)

def main():
    y = Solution()
    print(y.getRow(12))

if __name__ == "__main__":
    main()
