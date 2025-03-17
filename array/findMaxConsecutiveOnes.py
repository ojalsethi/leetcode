from typing import List
# Problem: Given a binary array, find the maximum number of consecutive 1's in this array.
# Approach: We can solve this problem using a simple linear scan through the array.
# We will maintain a count of the current number of consecutive 1's and update the maximum count whenever we encounter a 0.
# We also need to check at the end of the array in case the last element is a 1.
# Example:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The longest sequence of consecutive 1's is [1,1,1] which has a length of 3.
# Let's implement this in the function findMaxConsecutiveOnes.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Initialize variables to track the maximum count of consecutive 1's and the current count.
        max_cnt = 0  # Tracks the maximum number of consecutive 1's found so far.
        cnt = 0      # Tracks the current count of consecutive 1's.

        # Iterate through each number in the array.
        for num in nums:
            if num == 1:
                # If the current number is 1, increment the current count.
                cnt += 1
            else:
                # If the current number is 0, update the maximum count if needed
                # and reset the current count to 0.
                max_cnt = max(max_cnt, cnt)
                cnt = 0

        # After the loop, there might still be a sequence of 1's at the end of the array.
        # Compare max_cnt with cnt one last time to ensure the result is correct.
        return max(max_cnt, cnt)

# Time Complexity:
# The algorithm iterates through the array once, making it O(n), where n is the length of the array.

# Space Complexity:
# The algorithm uses a constant amount of space (only variables max_cnt and cnt), making it O(1).

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 0, 1, 1, 1]
    print(solution.findMaxConsecutiveOnes(nums))  # Output: 3
    nums = [0, 0, 0]
    print(solution.findMaxConsecutiveOnes(nums))  # Output: 0
    nums = [1, 1, 1, 1]
    print(solution.findMaxConsecutiveOnes(nums))  # Output: 4
    nums = [1, 0, 1, 1, 0, 1]
    print(solution.findMaxConsecutiveOnes(nums))  # Output: 2
