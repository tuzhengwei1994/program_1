#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 1、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
import os
def change_file_content(FileName, before, after):
    path = 'C:\\Users\\Administrator\\Desktop\\' + FileName
    with open(path, 'r') as f1, \
            open('C:\\Users\\Administrator\\Desktop\\user.txt.swap', mode='w') as write_f1:
        for line in f1:
            if before in line:
                line = line.replace(before, after)
            write_f1.write(line)
    os.remove(path)
    os.rename('C:\\Users\\Administrator\\Desktop\\user.txt.swap', path)


change_file_content(input('请输入需要修改的文件名'), input('请输入需要被修改的内容'), input('请输入修改的内容'))

# 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及【其他】的个数
def srting_count(str):
    number = 0
    Letter = 0
    space = 0
    another = 0
    for i in str:
        if i.isdigit():
            number += 1
        elif i.isalpha():
            Letter += 1
        elif i == ' ':
            space += 1
        else:
            another += 1
    print({'数字':number, '字母':Letter, '空格':space, '其他':another})


str = 'wee 121*ew d asd1  2d$'
srting_count(str)


# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def judge_lenth(obj):
    if len(obj) > 5:
        print('对象长度大于5')
    else:
        print('对象长度小于5')


judge_lenth('chgfgvg')


# 4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def func1(lst):
    if len(lst) > 2:
        return lst[:2]
    else:
        return  lst


lst = ['www4',5,8,9,'dsd',4]
print(func1(lst))


# 5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
def func2(obj):
    lst = []
    for i in range(len(obj)):
        if i%2 == 1:
            lst.append(obj[i])
    return lst


obj = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(func2(obj))


# 6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
def func3(dic={}):
    for i,j in dic.items():
        if len(j) > 2:
            dic[i] = j[:2]
    return dic


print(func3(dic={"a":"weqe", 'b':'s', 'c':'qq'}))