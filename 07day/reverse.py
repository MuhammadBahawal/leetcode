class Solution:
    def reverse(self, x):
        INT_MAX = 2147483647   
        INT_MIN = -2147483648  

        sign = 1
        if x < 0:
            sign = -1
            x = -x

        rev = 0
        while x != 0:
            pop = x % 10
            x = x / 10  
            if rev > (INT_MAX - pop) / 10:
                return 0

            rev = rev * 10 + pop

        rev = rev * sign
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev
