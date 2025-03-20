from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Initialize an empty list to store the results
        res = []
        
        # Define two pointers: left (l) starting at the beginning of the array
        # and right (r) starting at the end of the array
        l = 0
        r = len(nums) - 1
        
        # Loop until the two pointers meet
        while l <= r:
            # Calculate the square of the number at the left pointer
            sqr_l = nums[l] * nums[l]
            # Calculate the square of the number at the right pointer
            sqr_r = nums[r] * nums[r]
            
            # Compare the squares
            if sqr_r > sqr_l:
                # If the square of the right pointer is larger, append it to the result list
                res.append(sqr_r)
                # Move the right pointer one step left
                r -= 1
            else:
                # If the square of the left pointer is larger or equal, append it to the result list
                res.append(sqr_l)
                # Move the left pointer one step right
                l += 1
        
        # Reverse the result list to get the squares in non-decreasing order
        ans = res[::-1]
        return ans


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Mixed positive and negative numbers
    nums1 = [-4, -1, 0, 3, 10]
    print(f"Input: {nums1} -> Output: {solution.sortedSquares(nums1)}")
    # Expected Output: [0, 1, 9, 16, 100]

    # Test case 2: All negative numbers
    nums2 = [-7, -3, -1]
    print(f"Input: {nums2} -> Output: {solution.sortedSquares(nums2)}")
    # Expected Output: [1, 9, 49]

    # Test case 3: All positive numbers
    nums3 = [1, 2, 3, 4]
    print(f"Input: {nums3} -> Output: {solution.sortedSquares(nums3)}")
    # Expected Output: [1, 4, 9, 16]

    # Test case 4: Single element
    nums4 = [-5]
    print(f"Input: {nums4} -> Output: {solution.sortedSquares(nums4)}")
    # Expected Output: [25]

    # Test case 5: Already squared numbers in increasing order
    nums5 = [0, 1, 4, 9, 16]
    print(f"Input: {nums5} -> Output: {solution.sortedSquares(nums5)}")
    # Expected Output: [0, 1, 16, 81, 256]

    
# Time Complexity:

# The algorithm iterates through the array once using the two pointers, so the time complexity is 
# 𝑂
# (
# 𝑛
# )
# O(n), where 
# 𝑛
# n is the length of the input array.
# Space Complexity:

# The algorithm uses an additional list res to store the squared values. The space complexity is 
# 𝑂
# (
# 𝑛
# )
# O(n) due to the storage of results.