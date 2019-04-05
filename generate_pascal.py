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
        # need to calculate product first else the division can cause
        # rounding errors.  By calculating in this order we are also sure
        # that the numerator can be divided, without remainder, by the 
        # denominator.  Also, we need to alternate the product and division 
        # else the product/factorial in the numerator can also lead to 
        # numerical inaccuracies.
        for i in range(1,l+1):
            val *= (k+1-i)
            val /= i
        
        #print("{}C{} is {}".format(k+1,l+1,int(val)))
        return int(val)

def main():
    print("Debug line one")
    y = Solution()
    print(y.generate(12))

if __name__ == "__main__":
    main()
