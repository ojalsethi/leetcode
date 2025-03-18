
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Initialize a counter to track numbers with even digits
        cnt = 0
        
        # Iterate through each number in the input array
        for num in nums:
            digit_cnt = 0  # Initialize a counter for the number of digits
            
            # Calculate the number of digits in the current number
            while num > 0:
                digit_cnt += 1  # Increment digit counter
                num = num // 10  # Remove the last digit
            
            # Check if the number of digits is even
            if digit_cnt % 2 == 0:
                cnt += 1  # Increment the result counter if digits are even
        
        return cnt  # Return the total count of numbers with even digits
    
# Time Complexity:
# For each number in the array, the algorithm counts its digits using a while loop.
# Let 𝑑 be the average number of digits of a number in the array.
# The total number of operations is proportional to 𝑑×𝑛 where n is the length of the array.
# Thus, the time complexity is 𝑂(𝑛⋅𝑑)
  
# Space Complexity:
# The algorithm uses a constant amount of space for variables such as cnt and digit_cnt.
# Therefore, the space complexity is 𝑂(1).

# Test case 1: General case with mixed numbers
nums = [12, 345, 2, 6, 7896]
# Output: 2 (12 and 7896 have even digits)
print(Solution().findNumbers(nums))  # Expected output: 2

# Test case 2: All numbers have odd digits
nums = [123, 5, 7, 89, 111]
# Output: 0 (No numbers have an even number of digits)
print(Solution().findNumbers(nums))  # Expected output: 0

# Test case 3: All numbers have even digits
nums = [22, 4444, 66, 8888]
# Output: 4 (All numbers have an even number of digits)
print(Solution().findNumbers(nums))  # Expected output: 4

# Test case 4: Single number with even digits
nums = [44]
# Output: 1 (44 has an even number of digits)
print(Solution().findNumbers(nums))  # Expected output: 1

# Test case 5: Single number with odd digits
nums = [7]
# Output: 0 (7 has an odd number of digits)
print(Solution().findNumbers(nums))  # Expected output: 0

# Test case 6: Empty array
nums = []
# Output: 0 (No numbers to process)
print(Solution().findNumbers(nums))  # Expected output: 0