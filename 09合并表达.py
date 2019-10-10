#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 第一题：将names=['albert','james','kobe','kd']中的名字全部变大写
names = ['albert', 'james', 'kobe', 'kd']
res = map(lambda x: str.upper(x), names)
print(list(res))

# 第二题:将names=['albert','jr_shenjing','kobe','kd']中以shenjing结尾的名字过滤掉，然后保存剩下的名字长度
names = ['albert', 'jr_shenjing', 'kobe', 'kd']
res = filter(lambda x: x.endswith('shenjing') != True, names)
print(list(res))

# 第三题：求文件a.txt中最长的行的长度（按字符个数算，用max函数）
with open(r'C:\Users\Administrator\Desktop\a.txt', mode='r') as f1:
    print(len(max(f1, key=lambda x: len(x))))

# （1）求总共花了多少钱？
with open(r'C:\Users\Administrator\Desktop\shopping.txt', mode='r') as f2:
    sum_money = 0
    for i in f2:
        i = i.replace('\n', '')
        i = i.split(',')
        sum_money = int(i[1]) * int(i[2]) + sum_money
    print(sum_money)

# （2）打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]
with open(r'C:\Users\Administrator\Desktop\shopping.txt', mode='r') as f2:
    lst1 = []
    for i in f2:
        i = i.replace('\n', '')
        i = i.split(',')
        res = {'name': str(i[0]), 'price': i[1], 'count': i[2]}
        lst1.append(res)
    print(lst1)

# （3）求单价大于10000的商品信息,格式同上
res = filter(lambda x: int(x['price']) > 10000, lst1)
print(list(res))