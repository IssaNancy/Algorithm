# -*- encoding: utf-8 -*-
'''
@File    :   recursion.py   
@ModifyTime 2023/5/12 18:55      
@Author     Nancy
@Version    1.0
@Desciption solve a problem:a box contains boxes,and key is in one of the box,how to find it.
two ways:
    1) Loop:
        1.create a box stack;
        2.take out a box from box stack to find whether the key is in it;
        3.if it's also a box,then put it in the box stack;
        4.if it's a key,then end it.
        5.return 2;
    2) Recursion:
        1.check everything in the box;
        2.if it's a box,return 1;
        3.if it's a key,end it.
'''


