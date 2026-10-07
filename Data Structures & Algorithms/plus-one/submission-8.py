class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1

        if digits[i] == 9:
            while digits[i] == 9 and i>=0:
                digits[i] = 0
                i-=1
            if i == -1:
                digits.append(0)
                digits[0] =1
            else:
                digits[i]+=1
        else:
            digits[i]+=1

        return digits

        