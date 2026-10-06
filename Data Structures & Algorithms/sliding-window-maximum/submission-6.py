class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = 0

        for r in range(len(nums)):
            if q and l>q[0]:
                q.popleft()

            while q and nums[r]>nums[q[-1]]:
                q.pop()
            q.append(r)

            if (r-l+1) == k:
                output.append(nums[q[0]])
                l+=1
        return output

            


            
        




        