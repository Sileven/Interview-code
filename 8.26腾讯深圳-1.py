# coding=UTF-8
"""
 * n种二叉树？
 * 输入：节点数n
 * 输出：多少种不同的二叉树
 * 如：若n = 3，应输出5，因为三个节点的二叉树，共有5种可能：
 *   1         3     3      2      1
 *    \       /     /      / \      \
 *     3     2     1      1   3      2
 *   /     /       \                 \
 *  2     1         2                 3
 */
"""
import sys
n=int(sys.stdin.readline().strip())
count=[1]
for i in range(1,n+1):
    now=0
    for k in range(0,i):
        now+=count[k]*count[i-1-k]
    count.append(now)
print(count[n])