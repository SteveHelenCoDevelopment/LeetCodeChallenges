from memory_profiler import profile

@profile
def rotl(mylist,n):
    if ((n == 0) | (mylist == [])):
        return mylist
    n = n%len(mylist)
    return (mylist[n:len(mylist)] + mylist[0:n])


@profile
def find_min(mylist):
    ''' The objective of this function is to find the minimum value element
        in mylist - a list sorted in ascending order and then rotated by some
        aribtrary amount.  '''
        
    lp = 0   # left pointer
    rp = len(mylist)-1 # right pointer
    lp_old = 0   # saved left pointer
    
    while True:
        print("Debug 1 - lp:{0} rp:{1} lp_old:{2} mylist[{0}]:{3} and mylist[{1}]:{4}".format(lp,rp,lp_old,mylist[lp],mylist[rp]))
        if mylist[lp]>mylist[rp]:
            # moving RIGHT in the list
            if lp+1 >= rp:
                return mylist[rp] # found minimum
            lp_old = lp
            lp = int((lp+rp)/2)  # increase lp
        elif mylist[lp]==mylist[rp]:
            if lp+1 >= rp:
                return mylist[rp] # found minimum
            if lp>0:
                lp -= 1
                lp_old = lp
                rp -= 1  # decrement rp
        else:
            # moving LEFT in the list
            lp = int((lp_old+lp)/2)   # decrease lp
            rp = int((lp+rp)/2)       # and decrease rp
        if lp==rp:
            return mylist[rp]       # found minimum
    
def main():
    import cProfile
    #nums = [3,4,7,11,14,15,25,27,33,34,37,56,60,61,88,92,103]
    #nums = [10,1,10,10,10]
    #nums = [1,1,1]
    #nums = [2,0,1,1,1]
    nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,22,0,1,1,1]

    print("Nums = ", nums)
 #   cProfile.run('a = rotl(nums,0)')
 #   cProfile.run('a = rotl(nums,0)')
    
    #print("a = ",a)

 #   cProfile.run('print("Minimum of list is: {}".format(find_min(a)))')
    cProfile.run('find_min([4,5,7,11,1,3])')
    
if __name__ == "__main__":
    main()

