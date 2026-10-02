class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        seen = set()
        for i in range(len(nums)-2):
            target = -(nums[i])

            j = i+1
            k = len(nums)-1

            while j<k:
                curr = nums[j]+nums[k]
                if curr == target:
                    out = (nums[i], nums[j], nums[k])
                    if out not in seen:
                        output.append([nums[i], nums[j], nums[k]])
                    seen.add(out)
                    j+=1
                elif curr <target:
                    j+=1
                else:
                    k-=1
                    
        return output
        

        
        