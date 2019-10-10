#!/usr/bin/env python 
# -*- coding:utf-8 -*-
for i in range(1, 10):
    j = 1
    while j <= i:
        print(str(j) + 'x' + str(i) + '=' + str(i * j)+'\t',end='')
        j += 1
    print('')


for i in range(1, 10):
    for j in range(1, i+1):
        print(str(j) + 'x' + str(i) + '=' + str(i * j)+'\t', end='')
    print('')