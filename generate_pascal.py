class Solution():
    def generate(self, numRows):
        pt =[]
        for i in range(numRows):
            rowvals=[]
            for j in range(i+1):
                rowvals = rowvals + [self.calcNode(i,j)]
            pt.append(rowvals)
        return pt

    def calcNode(self,k,l):
        if (l == 0) or (l == k):
            return 1
        val = self.calcNode(k-1,l-1) + self.calcNode(k-1,l)
        return val

def main():
    print("Debug line one")
    y = Solution()
    print(y.generate(5))

if __name__ == "__main__":
    main()
