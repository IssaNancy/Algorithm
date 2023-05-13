# -*- encoding: utf-8 -*-
'''
@File    :   selection_sort.py
@ModifyTime 2023/5/12 17:49      
@Author     Nancy
@Version    1.0
@Desciption
'''


def findSmallest(array):
    '''

    :param array:
    :return:
    '''
    smallest = array[0]  # store the smallest value
    smallest_index = 0  # store the index of the smallest value
    for i in range(1,len(array)):
        if array[i] <smallest:
            smallest_index=i
            smallest=array[i]
    return smallest_index

def selectionSortA(array):
    '''
    sort the array
    :param array: array needed to be sorted
    :return:
    '''
    new_array=[]
    for i in range(len(array)):
        smallest=findSmallest(array)
        new_array.append(array.pop(smallest))
    return new_array

def selectionSortB(array):
    '''
    自己的优化
    :param array:
    :return:
    '''
    for i in range(len(array)):
        smallest_index=findSmallest(array[i:])+i
        if i!=smallest_index:
            temp=array[smallest_index]
            array[smallest_index]=array[i]
            array[i]=temp
    return array

print(selectionSortA([1,2,0,4,3,5,7,8]))
print(selectionSortB([1,2,0,4,3,5,7,9]))
