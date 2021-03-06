'''
这是nester.py模块，提供了一个名为print_lol()的函数，这个函数的作用是打印列表，其阿红有可能包含（也可能不包含）嵌套列表
'''
import sys

def print_lol( the_list,indent=False,level=0,output=sys.stdout ):
    '''
    这个函数取一个位置参数，名为the_list，这可以是任何python列表，也可以是包含嵌套列表的列表。所指定的列表中的每个数据项会递
    归地输出到屏幕上，各数据各占一行
    '''

    for each_item in the_list:
        if isinstance( each_item,list ):
            print_lol( each_item,indent,level+1,output )
        else:
            if indent==True:
                for num in range(level):
                    print( '\t',end='',file=output )
            print(each_item,file=output )