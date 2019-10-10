#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sys,shutil

# 练习一：不改变内容顺序，去除文件中重复的行
with open(r'C:\Users\Administrator\PycharmProjects\untitled\foo.txt', 'r') as f1_read,\
        open(r'C:\Users\Administrator\PycharmProjects\untitled\foo2.txt', 'w') as f2_write:
    s = set()
    for line in f1_read:
        if '\n' in line:
            print(line)
            line2 = line.replace('\n', '')
        if line not in s:
            s.add(line)
            f2_write.write(line)
# 练习二：写一个在终端执行拷贝文件的命令，文件不仅限于文本文件，要求是：在终端环境下输入命令：
# python文件路径 源文件路径 目标文件路径

# alu_path = sys.argv[0]
# print(alu_path)
# src = input("请输入源文件地址：")
# dst = input('请输入目标文件地址:')
# info1 = '%s' % src
# info2 = '%s' % dst
# shutil.copyfile(info1, info2)
lst = sys.argv  # 把命令行中解释器后空格分开的所有参数都存成列表
src_path = lst[1]
dst_path = lst[2]
with open(src_path, 'rb') as f1:
    with open(dst_path, 'wb') as f2:
        for line in f1:
            f2.write(line)

# 练习三：修改文件，原内容不能覆盖，修改后字符之间的空格不能变化
with open(r'C:\Users\Administrator\PycharmProjects\untitled\05-03.txt', 'r') as f3, \
        open(r'C:\Users\Administrator\PycharmProjects\untitled\05-03-2.txt', 'w') as f4:
    content = f3.read()
    print(content)
    keyword = input('请输入关键字：')
    add_content = input('请输入添加内容：')
    post = content.find(keyword)
    if post != -1:
        content = content[:post + len(keyword)] + add_content + content[post + len(keyword):]
    f4.write(content)

