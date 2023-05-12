# -*- encoding: utf-8 -*-
'''
@File    :   binary_search.py
@ModifyTime 2023/5/9 12:00      
@Author     Nancy
@Version    1.0
@Desciption: 二分查找，输入必须是一个有序的元素列表，如果要查找的元素包含在列表中，二分查找返回其位置，否则返回null
'''

def binary_search(list,item):
  '''
  :param list:输入一个有序列表
  :param item:查找的元素
  :return:该元素在list中的位置   或   null
  '''
  low=0
  high=len(list)-1
  while low <= high:
      mid = (low + high) // 2
      guess=list[mid]
      if guess<item:
          low=mid+1
          print('mid=',mid)
      if guess >item:
          high=mid-1
          print('mid=', mid)
      else:
          return mid
  return None
if __name__=='__main__':
    list=[i for i in range(100)]
    print(binary_search(list,0))

