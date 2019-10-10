#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 练习一：
sys_name = 'Albert'
sys_password = '1'
while True:
    user_name = input('请输入用户名：')
    user_password = input('请输入密码：')
    if user_name != sys_name or user_password != sys_password:
        print('用户名或密码错误')
        continue
    else:
        print('登录成功')
        break

# 练习二
power = input('请输入您的用户名：')
if power == 'Albert':
    print('您的权限是超级管理员')
elif power == 'tom':
    print('您的权限是普通管理员')
elif power == ('jack' or 'rain'):
    print('您的权限是业务主管')
else:
    print('您的权限是普通用户')

# 练习三：
today = input('请输入今天的星期数：')
if today == 'monday' or 'tuesday' or 'wednesday' or 'thursday' or 'friday':
    print('上班')
elif today == 'saturday' or 'sunday':
    print('出去浪')
else:
    print('输入异常')

# 练习四：
sys_name = 'Albert'
sys_password = '1'
times = 0
while True:
    if times < 3:
        user_name = input('请输入用户名：')
        user_password = input('请输入密码：')
        if user_name != sys_name or user_password != sys_password:
            print('用户名或密码错误')
            times += 1
            continue
        else:
            print('登录成功')
            times = 0
            if input('退出请按q：') == 'q':
                break
    else:
        break

# 练习五：
sys_age = 25
times = 0
while True:
    if times < 3:
        user_age = input('请输入年龄：')
        if not user_age.isdigit():
            print('输入异常，重新输入')
            continue
        if int(user_age) != sys_age:
            times += 1
            print('错误，请重新输入，还有%d次机会' %(3-times))
            continue
        else:
            print('正确')
            break
    else:
        again = input('继续请输入Y或y，退出请输入N或n：')
        if again == 'Y' or 'y':
            times = 0
            continue
        elif again == 'n' or 'N':
            break

# 练习六：
i = 1
while True:
    if i < 11:
        if i != 7:
            print(str(i)+' ',end='')
        else:
            print('  ',end='')
        i += 1
    else:
        break

# 1--100的和
lst = []
for j in range(1,101):
    lst.append(j)
print(sum(lst))

# 1--100的所有奇数
for k in range(1, 101, 2):
    print(k)

# 1--100的所有偶数
for m in range(2, 101, 2):
    print(m)

#求1-2+3-4...+99的值
lst1 = []
lst2 = []
for k in range(1, 101, 2):
    lst1.append(k)
for m in range(2, 100, 2):
    lst2.append(m)
result = sum(lst1)-sum(lst2)
print(result)

# 练习七
n = int(input('请输入层数：'))
for i in range(1,n+1):
        print(('*'*(2*i-1)).center(2*n-1))