# coding=utf-8
# 二分查找第一次出现和最后出现的位置 然后相减就是次数

class Solution(object):
    def searchRange(self, nums, target):
        # 二分查找
        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) / 2
                if x > A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1  # x==x[mid]mid也要前移  因为要找最左边
            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) / 2
                if x >= A[mid]:
                    left = mid + 1   # 因为要找到最后一个target值，所以mid与target相等，也需要后移mid
                else:
                    right = mid - 1
            return right

        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]


s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))