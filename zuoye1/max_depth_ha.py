# -*- coding: utf-8 -*- 
# @Time : 2022/3/14 18:59 
# @Author : Administrator 
# @Email : o65790uu@qq.com 
# @File : max_depth_ha.py 
# 类的定义如下
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

def maxDepth(root):
    if root is None:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1



# 函数调用格式如下
def main():
    root = TreeNode(5)
    res = maxDepth(root)
    print(res)

if __name__ == '__main__':
    main()
