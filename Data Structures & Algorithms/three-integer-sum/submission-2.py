class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #handling duplicates is the main issue
        dicti = {}
        for i in range(len(nums)):
            dicti[nums[i]] = i
        dupli = set()

        output = []

        for i in range(len(nums)):
            target = -(nums[i])
            for j in range(i+1, len(nums)):
                tar = target - nums[j]
                if tar in dicti and (dicti[tar]!=j and dicti[tar]!=i):
                    numbers = [nums[i], nums[j], tar]
                    numbers.sort()
                    if tuple(numbers) in dupli:
                        continue
                    dupli.add(tuple(numbers))
                    output.append(numbers)

        return output
            
        
        

        
        