class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If mid element is greater than the rightmost element, the pivot is on the right side
            if nums[mid] > nums[right]:
                left = mid + 1
            # If mid element is less than or equal to the rightmost element, the pivot is on the left side
            else:
                right = mid
        
        # Left will point to the minimum element
        return nums[left]

# driver code
nums = [3,4,5,1,2]
obj = Solution()
obj.findMin(nums)
