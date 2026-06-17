class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #need to find the product of array except self\
        #some kind of prefix or suffix to be used
        prefix = [1]*len(nums)
        multi = 1
        for i in range(len(nums)-1):
            multi*=nums[i]
            prefix[i+1] = multi
        
        suffix = [1]*len(nums)
        multi = 1
        for i in range(len(nums)-1, 0, -1):
            multi*=nums[i]
            suffix[i-1] = multi
        
        output = [1]*len(nums)
        for i in range(len(nums)):
            output[i] = prefix[i]*suffix[i]
        
        return output
            

            
            
            
            

        
            
        