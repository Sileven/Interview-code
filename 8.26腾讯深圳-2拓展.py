#!/usr/local/bin/python
# coding=UTF-8
'''
@Usage: 
@author: rikysi
@Date: 2019-08-26 14:41:01
@LastEditors: rikysi
@LastEditTime: 2019-08-26 15:16:11
'''
"""
输入一个有序数组，删除数组所有相同元素，返回去重后的数组
如：
输入 [1, 2, 2, 3]
输出 [1, 2, 3]
要求：不能使用python自带的和数组操作相关的函数
"""
# 方案1，直接赋值
import sys
nums=[int(m) for m in sys.stdin.readline().split()]

if len(nums)<2:
    print(nums)
    exit(0)

start=1
end=1
            
while(end<len(nums)):     
    if nums[end]!=nums[start-1]:
        nums[start]=nums[end]
        start+=1
    end+=1

print(nums[:start])

#方案2，交换
# import sys
# nums=[int(m) for m in sys.stdin.readline().split()]

# if len(nums)<2:
#     print(nums)
#     exit(0)

# last=nums[0]
# start=1
# end=1
            
# while(end<len(nums)):     
#     while(end<len(nums) and nums[end]==last):
#         end+=1
#     last=nums[end]
    
#     if start<end:
#         tmp=nums[start]
#         nums[start]=nums[end]
#         nums[end]=tmp
    
#     start+=1
#     end+=1
# print(nums[:start])
    