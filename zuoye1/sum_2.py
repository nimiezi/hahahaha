# -*- coding: utf-8 -*- 
# @Time : 2022/3/14 19:12 
# @Author : Administrator 
# @Email : o65790uu@qq.com 
# @File : sum_2.py
def hasSum(array, target_number):
    for index, num in enumerate(array):
        find = target_number - num
        if find in array and find != num:
            return 1, num, find

# 函数调用格式如下
def main():
    array = [1, 5, 7, 3]
    target_number = 10
    result, a, b = hasSum(array, target_number)
    if result == 1:
        print('YES, %d + %d = %d' % (a, b, target_number))
    else:
        print('NO')


if __name__ == '__main__':
    main()
