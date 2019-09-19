# coding=utf-8
# 左右分别维护最大/小堆

def max_min_dui(a, left, right):
    # left right 是左右最大/小堆  a是新进来的数
    if (len(left) + len(right)) & 1 == 0:  # &1==0则是偶数
        if left and a < max(left):
            left.append(a)
            a = max(left)
            left.remove(a)
        right.append(a)   # 左边加一个，则把最大的弹出给右边 左右个数相等
    else:   # 当前个数为奇数，默认左边多一个 则新的数考虑放右边去
        if right and a > min(right):
            right.append(a)
            a = min(right)
            right.remove(a)  # 右边把最小值弹出，给到左边去
        left.append(a)
    return left, right  # 返回一个数进来后，调整好的左右堆

def main(arrs):
    left, right = [],[]
    for i in range(len(arrs)):
        left, right = max_min_dui(int(arrs[i]), left, right)
    if len(arrs) & 1 == 0:
        res = (max(left) + min(right))/2
    else:
        res = min(right)  # 注意是右边的最小堆会多一个数
        # 应该是因为最先是right开始add数进来吧...
    return res

in_datas = raw_input()
arrs = in_datas.split(' ')
ans = main(arrs)
print ans