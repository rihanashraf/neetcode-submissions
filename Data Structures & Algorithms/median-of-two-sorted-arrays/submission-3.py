class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #two partitions
        total = len(nums1)+len(nums2)
        half = total//2

        A, B = nums1, nums2

        if len(B)<len(A):
            A, B = B, A

        l, r = -1, len(A)-1

        while l<=r:
            m = (l+r)//2
            n = half - m -2

            a = A[m] if m >=0 else float("-infinity")
            b = A[m+1] if m+1<len(A) else float("infinity")
            c = B[n] if n >=0 else float("-infinity")
            d = B[n+1] if n+1<len(B)else float("infinity")

            #check if the partition is correct

            if a<=d and c<=b:
                if total%2==0:
                    return (max(a,c)+min(b,d))/2
                else:
                    return min(b, d)

            elif a>d:
                r = m-1
                print("yes")
            else:
                l=m+1









