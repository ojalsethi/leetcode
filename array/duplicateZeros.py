class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # Step 1: Count the number of zeros in the array
        zero_count = 0
        original_length = len(arr)
        
        for element in arr:
            if element == 0:
                zero_count += 1
        
        # Step 2: Extend the array by appending zeros for duplication logic
        arr.extend([0] * zero_count)
        new_end = len(arr) - 1  # Updated length after appending zeros

        # Step 3: Work backwards to shift elements and duplicate zeros
        for i in range(original_length - 1, -1, -1):
            arr[new_end] = arr[i]  # Copy element to its new position
            new_end -= 1

            if arr[i] == 0:
                arr[new_end] = 0  # Duplicate zero
                new_end -= 1

        # Step 4: Remove extra elements to restore the original length
        while len(arr) > original_length:
            arr.pop()


# O(n) (linear time)
# O(1) (ignoring the input array)