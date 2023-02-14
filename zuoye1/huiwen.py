# -*- coding: utf-8 -*- 
# @Time : 2022/3/14 19:23 
# @Author : Administrator 
# @Email : o65790uu@qq.com 
# @File : huiwen.py
# def longestPalindrome(s):
#     if len(s) == 1 or s == s[::-1]:
#         return len(s)
#     else:
#         init_len = 1
#         for i in range(1, len(s)):
#             if i - init_len - 1 >= 0 and s[i - init_len - 1: i + 1] == s[i - init_len - 1: i + 1][::-1]:
#                 init_len += 2
#             elif i - init_len >= 0 and s[i - init_len: i + 1] == s[i - init_len: i + 1][::-1]:
#                 init_len += 1
#     return init_len


def longestPalindrome(s):
    firststr = ''
    secondstr = ''
    for each in range(len(s) if len(s) < 1000 else 1000):
        m, n = each, each
        while m >= 0 and n <= len(s) - 1 and s[m] == s[n]:
            if len(firststr) <= n - m + 1:
                firststr = s[m:n + 1]
            m -= 1
            n += 1
        m, n = each, each + 1
        while m >= 0 and n <= len(s) - 1 and s[m] == s[n]:
            if len(secondstr) <= n - m + 1:
                secondstr = s[m:n + 1]
            m -= 1
            n += 1
    return firststr if len(firststr) > len(secondstr) else secondstr


# 函数调用格式如下
def main():
    s = "helloollyyd"
    res = longestPalindrome(s)
    print("res=", res)


if __name__ == '__main__':
    main()
