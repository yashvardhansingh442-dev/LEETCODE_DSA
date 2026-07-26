class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow (32-bit signed int range)
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign of result
        negative = (dividend < 0) != (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple
        
        return -result if negative else result