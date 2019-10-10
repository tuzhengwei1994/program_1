#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import time
# 1、 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）。要求：登录成功一次，后续的函数都无需再输入用户名和密码；注意：从文件中读出字符串形式的字典，可以用以下方式把字典字符串转化成字符串
# eval('{"name":"albert","password":"123"}')
current_user = {'username': None, }
def func1(fn):
    def func2(*args, **kwargs):  # 有参和无参都不影响
        if current_user['username']:  # 登录成功标志位
            print(current_user['username'])
            print('您已经登陆过，无需再次登录')
            fn(*args, **kwargs)
            return
        username_input = input('请输入账号：').strip()
        password_input = input('请输入密码：').strip()
        with open(r'C:\Users\Administrator\Desktop\123.txt', 'r') as f1:
            for line in f1:
                if eval(line)['name'] == username_input and eval(line)['password'] == password_input:
                    print('登陆成功')
                    current_user['username'] = username_input
                    fn(*args, **kwargs)
                return
    return  func2


@func1
def func3():
    print('函数3')


@func1
def func4(*args):
    print('函数4', *args)


func3()
func4('跳过登录')

# 2、编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录
interval_time = {'time': 0, }
stop_time = {'time': 0, }
start_time= {'time': 0, }

def func1(fn):
    def func2(*args, **kwargs):  # 有参和无参都不影响
        if interval_time['time'] > 3 or interval_time['time'] == False:
            username_input = input('请输入账号：').strip()
            password_input = input('请输入密码：').strip()
            with open(r'C:\Users\Administrator\Desktop\123.txt', 'r') as f1:
                for line in f1:
                    if eval(line)['name'] == username_input and eval(line)['password'] == password_input:  # eval 方法能使字符串本身的引号去掉，保留字符的原本属性。
                        print('登陆成功')
                        start_time['time'] = time.time()
                        interval_time['time'] = username_input
        fn(*args, **kwargs)
        stop_time['time'] = time.time()
        interval_time['time'] = (stop_time['time'] - start_time['time'])
    return func2


@func1
def func3():
    print('功能3运行中')
    time.sleep(3.1)


@func1
def func4(*args):
    print('功能4运行中', *args)
    time.sleep(2)

@func1
def func5(*args):
    print('功能5运行中', *args)
    time.sleep(2)


func3()
func4()
func5()

# 3、编写日志装饰器，实现功能：一旦某函数执行，则将函数执行时间写入到日志文件中，日志文件路径可以指定。
# 注意：时间格式的获取
def func6(fn):
    def func7(*args, **kwargs):
        start_time = time.time()
        fn()
        stop_time = time.time()
        interval_time = stop_time - start_time
        path = input('请指定文件路径：')
        content = '程序运行了' + str(interval_time) + '秒' + '\n'
        with open(path, 'a') as f2:
            f2.write(content)
    return func7

@func6
def func8():
    print('功能8运行中')
    time.sleep(3)


