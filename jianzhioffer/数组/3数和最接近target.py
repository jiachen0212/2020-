# coding=utf-8
# a + b + c closest to target   三指针法
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()  # 数组先排序
        res = sum(nums[0: 3])
        diff = abs(res - target)
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1    # ijk三指针
            if nums[i] * 3 - target > diff:
                break
            while j < k:
                r = nums[i] + nums[j] + nums[k]
                if abs(r - target) < diff:
                    res = r
                    diff = abs(r - target)
                if r > target:
                    k = k - 1
                elif r < target:
                    j = j + 1
                else:  # r==target
                    return r
        return res
