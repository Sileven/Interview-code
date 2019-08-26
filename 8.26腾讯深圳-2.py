#!/usr/local/bin/python
# coding=UTF-8
'''
@Usage: 
@author: rikysi
@Date: 2019-08-26 14:41:01
@LastEditors: rikysi
@LastEditTime: 2019-08-26 15:37:04
'''
"""
输入一个有序数组，删除数组所有相同元素，返回去重后的数组
如：
输入 [1, 2, 2, 3]
输出 [1, 2, 3]
要求：不能使用python自带的和数组操作相关的函数
"""
import sys
nums=[int(m) for m in sys.stdin.readline().split()]

if len(nums)<2:
    print(nums)
    exit(0)

start=1
end=1
            
while(end<len(nums)):     
    if nums[end]!=nums[start-1]:
        if end==len(nums)-1 or (end!=len(nums)-1 and nums[end]!=nums[end+1]):
            nums[start]=nums[end]
            start+=1    
    end+=1

print(nums[:start])
    