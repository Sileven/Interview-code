#!/usr/local/bin/python
# coding=UTF-8
"""
输入一个有序数组，删除数组所有相同元素，返回去重后的数组
如：
输入 [1, 2, 2, 3]
输出 [1, 3]
要求：不能使用python自带的和数组操作相关的函数
"""
import sys
nums=[int(m) for m in sys.stdin.readline().split()]

if len(nums)<2:
    print(nums)
    exit(0)

start=0
            
for end in range(0,len(nums)):
    flag=True
    if end>0 and nums[end]==nums[end-1]:
        flag=False
    if end<len(nums)-1 and nums[end]==nums[end+1]:
        flag=False

    if flag:
        nums[start]=nums[end]
        start+=1
print(nums[:start])
    