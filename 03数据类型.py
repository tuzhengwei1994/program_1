#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 练习一：
name = ' alberT'
print(name.strip())
print(name.startswith('al'))
print(name.endswith('T'))
print(name.replace('l', 'p'))
print(name.split('l'))
print(name.upper())
print(name.lower())
print(name[1])
print(name[:3])
print(name[-2:])
print(name.find('e'))
print(name.replace(name[-1],''))

# 练习二
list1 = ['albert', 18, [2000, 1, 1]]
list1_name = list1[0]
list1_age = list1[1]
list1_year = list1[2][0]
list1_month = list1[2][1]
list1_day = list1[2][2]

# 练习三
list2 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
dict1 = {'k1': list2[0:5], 'k2': list2[6:]}

# 练习四
# 4.1
list2 = ['a', 'b', 1, 'a', 'a']
set1 = set(list2)
list3 = []
for i in set1:
    list3.append(i)
print(list3)

# 4.2
list4 = []
for i in list2:
    if i not in list4:
        list4.append(i)
print(list4)

# 4.3
list5 = [
    {'name': 'albert', 'age': 18, 'sex': 'male'},
    {'name': 'james', 'age': 35, 'sex': 'male'},
    {'name': 'taylor', 'age': 25, 'sex': 'female'},
    {'name': 'albert', 'age': 18, 'sex': 'male'},
    {'name': 'albert', 'age': 18, 'sex': 'male'}
]
list6 = []
for i in list5:
    if i not in list6:
        list6.append(i)
print(list6)

# 练习五
s = "hello albert albert say hello world world"
# 方法一
dict2 = {'hello': s.count('hello'),
         'albert': s.count('albert'),
         'say': s.count('say'),
         'world': s.count('world')}
print(dict2)
# 方法二
dict3 = {}
for word in s.split(' '):
    if word in dict3.keys():
        dict3[word] += 1
    else:
        dict3[word] = 1
print(dict3)

# 练习六
goods_dic = {'apple': 10,
             'mac': 10000,
             'iphone': 8000,
             'lenovo': 30000,
             'chicken': 10
}
print('goods_dic=', goods_dic)
goods_list = []
while True:
    goods_dic2 = {}
    goods_name = input('请输入商品名：')
    if not goods_name or goods_name not in goods_dic.keys():
        continue
    goods_dic2['name'] = goods_name
    goods_dic2['price'] = goods_dic[goods_name]
    goods_num_str = input('请输入购买数量：')
    if not goods_num_str or not goods_num_str.isdigit():
        continue
    goods_num_int = int(goods_num_str)
    goods_dic2['quantity'] = goods_num_int
    goods_list.append(goods_dic2)
    break
print(goods_list)

