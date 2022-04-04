# -*- coding = utf-8 -*-
# @Time : 2022/4/4 22:46
# @Author :蒋大帅
# @File : 购物车练习.py
# @Software:PyCharm

i=0
products=[['ipone',6888],['Macpro',14800],['小米',2499],['Coffee',31],['Bool',60],['Nike',699]]
print('-------商品列表-------')
for produce in products:
    print(i,end='\t')
    i+=1
    for index in produce:
        print(index,end='\t')
    print('\n')

shoppings=[]
i=input('请告诉我你想买什么：')
while i!='q':
    shoppings.append(products[int(i)][0])
    i=input("你还要买啥，不买的话输入'q'")
    if i=='q':
        print('你要买的商品为：')
        for shopping in shoppings:
            print(shopping)
