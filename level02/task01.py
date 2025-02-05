"""
!/usr/bin/python3.10
-*- coding: utf-8 -*-
@Time    : 2025/2/5 21:25
@Author  : wonderbell
@Email   : 969064814@qq.com
@File    : task01.py
@Software: PyCharm
@description: leetcode: https://leetcode.cn/problems/ransom-note/description/
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_list = list(magazine)
        for item in ransomNote:
            if item in m_list:
                m_list.remove(item)
            else:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    ransomNote = "aa"
    magazine = "ab"
    res = solution.canConstruct(ransomNote, magazine)
    print(res)
