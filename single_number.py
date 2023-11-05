class Solution(object):
    def singleNumber(self, nums):
        n=len(nums)
        for i in range(0,n):
            flag=0
            for j in range(i+1,n):
                if(nums[i]==nums[j]):
                    flag=1
                    break
            if(flag==0):
                number= nums[i]
                break
        return number 