# coding=utf-8
'''
云从nlp算法题
盛最多水的容器
'''
class Solution(object):
    def maxArea(self, height):
            i = 0
            j = len(height)-1
            water = 0
            while i<j:
                water = max(water,(j-i)*min(height[i],height[j]))
                if height[i]<height[j]:
                    i+=1
                else:
                    j-=1
            return water


