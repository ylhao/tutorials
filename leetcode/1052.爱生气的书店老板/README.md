# 解题思路

1. 先计算所有老板没有生气时候的客气
2. 计算从 0 ~ X 老板不生气增加的客人数
3. 滑动窗口，当前是 0 ~ X,下一时候是 1 ~ X+1，计算 i ~i+X 窗口内老板不生气增加的客人数，并且记录最大值
[题目链接](https://leetcode-cn.com/problems/grumpy-bookstore-owner/submissions/)