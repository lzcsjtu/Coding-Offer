#!/usr/bin/env python
# coding: utf-8

# In[4]:


#coding=utf-8
'''
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，
也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 

限制：
2 <= n <= 100000
'''
from typing import List


# In[5]:


#排序 先排序，然后看相邻元素是否有相同的，有直接return。 修改了原数据
#时间O(nlogn)了，空间O(1)

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]
        n = len(nums)
        for index in range(1, n):
            if pre == nums[index]:
                return pre
            pre = nums[index]


# In[9]:


#哈希表 时间O(n)，空间O（n），不修改原数据
'''
1.初始化： 新建 HashSet ，记为 dic ；
2.遍历数组 nums 中的每个数字 num ：
    1.当 num 在 dicdic 中，说明重复，直接返回 num；
    2.将 num 添加至 dic中；
3.返回 -1。本题中一定有重复数字，因此这里返回多少都可以。

'''

class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        dic = set()
        for num in nums:
            if num in dic: return num
            dic.add(num)
        return -1
    


# In[ ]:


#集合法，时间O(n),空间O(n),不修改原数据。

'''
构建一个新的空集合，然后依次添加元素
当发现某个元素已存在时，则说明该元素重复了。具有普适性
也可用字典替换集合，本质相同。
'''
class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        dic = set()
        for i in range(len(nums)):
            dic.add(nums[i])
            if len(dic)<i+1:
                return nums[i]


# In[11]:


#原地哈希法，修改了原数组
#时间复杂度 O(N) ： 遍历数组使用 O(N)，每轮遍历的判断和交换操作使用 O(1)。
#空间复杂度 O(1) ： 使用常数复杂度的额外空间。

'''题目说明尚未被充分使用，即在一个长度为n的数组nums里的所有数字都在0~n-1的范围内。
此说明含义：数组元素的 索引 和 值 是 一对多 的关系。
因此，可遍历数组并通过交换操作，使元素的 索引 与 值 一一对应
（即nums[i] = i）。因而，就能通过索引映射对应的值，起到与字典等价的作用。

遍历数组 nums ，设索引初始值为 i = 0:

若 nums[i] = i： 说明此数字已在对应索引位置，无需交换，因此跳过；
若 nums[nums[i]] = nums[i]： 代表索引 nums[i]处和索引 i处的元素值都为 nums[i] ，
即找到一组重复值，返回此值 nums[i]；
否则： 交换索引为 i 和 nums[i]的元素值，将此数字交换至对应索引位置。
若遍历完毕尚未返回，则返回 -1。
'''
class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1


# In[28]:



#二分查找，时间O(nlongn),空间O(1),不修改原数据。

'''
该方法对于本题不适用，但是题目类似
长度为n的数组，且数字都在1~n-1之间，且一定有数字是重复的。
每一遍二分的过程，统计nums元素中1~m的数量(m <=n-1, 改变m的值，遍历的是整个数组)，
如果数量大于这个值，这说明重复的元素一定在1~m中。
但实际此种方法不可行，例如[1, 1, 1, 2, 4, 5, 6, 7, 8, 9]，
对这个样例，则无法找到正确的答案。
'''

class Solution:
    def findRepeatNumber(self, nums:List[int]) -> int:
        # 注意初始值是1
        min_value = 1
        max_value = len(nums) - 1
        while (max_value > min_value):
            mid_value = (max_value + min_value) // 2
            counts = self.countNums(nums, min_value, mid_value);
            if counts > mid_value - min_value + 1:
                max_value = mid_value
            else:
                # 注意这个地方需要加1，不然最后会陷入死循环，比如最后max_value为2,min_value为1，则会一直循环,对应的上面也可以给max_value复制的地方减1
                min_value = mid_value + 1
        # 跳出循环的条件一定是max_value = min_value
        return min_value

    def countNums(self, nums, min_value, max_value):
        count = 0
        for ele in nums:
            if min_value <= ele <= max_value:
                count += 1
        return count


# In[35]:


if __name__ == "__main__":
    head1 = [1, 2, 4,2]
    solution = Solution()
    sorted_lists = solution.findRepeatNumber(head1)
    print(sorted_lists)


# In[ ]:




