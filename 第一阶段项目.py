#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# 项目一：多级菜单
goods_calss = ['car', 'phone', 'camera']
car_brand = ['BMW', 'Benz', 'Audi']
car_model = [['X1','X3','X5','X7'],
             ['S300L', 'S350L', 'S400L', 'S500L', 'S600L'],
             ['A3', 'A4', 'A5', 'A6', 'A8'],
             ]
flag = True
while flag:
    print(goods_calss)
    command = input('返回请按b,退出请按q,选择条目进入下一页')
    if command == 'b':
        break
    elif command == 'q':
        flag = False
    elif command == 'car':
        while flag:
            print(car_brand)
            command = input('返回请按b,退出请按q,选择条目进入下一页')
            if command == 'b':
                break
            elif command == 'q':
                flag = False
            elif command == 'BMW':
                while flag:
                    print(car_model[0])
                    command = input('返回请按b,退出请按q')
                    if command == 'b':
                        break
                    elif command == 'q':
                        flag = False
            elif command == 'Benz':
                while flag:
                    print(car_model[1])
                    command = input('返回请按b,退出请按q')
                    if command == 'b':
                        break
                    elif command == 'q':
                        flag = False
            elif command == 'Audi':
                while flag:
                    print(car_model[2])
                    command = input('返回请按b,退出请按q')
                    if command == 'b':
                        break
                    else:
                        flag = False

# 项目二
import re
flag = True
goods_dic = {'1 ipad': 4000,
             '2 mac': 10000,
             '3 iphone': 8000,
             '4 lenovo': 6000,
             '5 bike': 1000
             }
attention = input('若有账号，则输入登录，若无账号，则输入注册')
if attention == '登录':
    times = 0
    while flag:
        with open(r'C:\Users\Administrator\PycharmProjects\untitled\深度之眼\账户信息.txt', 'r') as f1, \
                open(r'C:\Users\Administrator\PycharmProjects\untitled\深度之眼\黑名单.txt', 'a+') as f2:
            user_name = input('请输入你的登录账号：')
            user_password = input('请输入你的密码：')
            f2.seek(0, 0)
            if user_name in f2.read():  # 如果账号在黑名单中，则退出
                print('该用户已经列入黑名单，无法登陆')
                break
            for line in f1:
                if user_name in line:  # 判断账号是否存在
                    get = '1'  # 账号存在标志位
                    content = line.split('|')
            if user_password == content[1]:  # 验证密码
                user_money = content[2]
                print('登录成功')
                print('您的余额为:' + content[2] + "开始购物吧")
                print(goods_dic)
            elif get != '1' or user_password != content[1]:  # 如果账号不存在或者密码不正确
                times += 1
                if times < 3:
                    print('1')
                    print("密码错误，你还有%d次机会" % (3 - times))
                    continue
                else:
                    f2.writelines(user_name)  # 失败超过3次，把账号列入黑名单
        break
elif attention == '注册':
    while flag:
        user_name = input('请输入你的注册账号：')
    # 密码输入判断
        while flag:
            user_password = input('请输入你的密码：')
            again = input('请再次输入你的密码：')
            if user_password != again:
                print('两次密码不一致，请重新输入')
                continue
            else:
                break
    # 打开文件,判断账号是否存在
        f1 = open(r'C:\Users\Administrator\PycharmProjects\untitled\深度之眼\账户信息.txt', 'a+')
        f1.seek(0, 0)
        if user_name not in f1.read():
            print('注册成功')
            break
        else:
            print('账号已存在，请重新输入')
            continue
# 写入余额
    while flag:
        user_money = input('请输入您的余额：')
        if not user_money.isdigit():
            print('请不要输入数字以外的字符')
            continue
        information = user_name + '|' + user_password + '|' + user_money + '\n'
        print(information)
        f1.writelines(information)
        break
    f1.close()
    print('开始购物吧')
    print(goods_dic)
else:
    flag = False
goods_list = []
# 判断余额，并记录购买的商品和余额
while flag:
    choice = input('请选择购买的商品的序号:')
    for key in goods_dic.keys():
        if choice in key:
            price = goods_dic[key]
            if int(price) <= int(user_money):
                user_money_new = str(int(user_money)-int(price))
                goods_list.append(key)
            else:
                print('账户余额不足，无法购买')
                goods_list.append('账户余额：' + user_money_new)
                print(goods_list)
                flag = False
# 修改文本中对应账户的余额
            while flag:
                str1 = ""
                with open(r'C:\Users\Administrator\PycharmProjects\untitled\深度之眼\账户信息.txt', 'r') as f4:
                    for line2 in f4:
                        if user_name in line2:
                            line3 = re.sub(user_money, user_money_new, line2)
                            user_money = user_money_new
                            str1 += line3
                        else:
                            str1 += line2
                with open(r'C:\Users\Administrator\PycharmProjects\untitled\深度之眼\账户信息.txt', 'w') as f3:
                    f3.write(str1)
                    break

