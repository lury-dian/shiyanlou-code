#! /usr/bin/env python3
"""
首先根据输入的菜单得到购物清单
"""

foodlist = input("Please enter the food you need to bug: ")
print(foodlist)
shoplist = foodlist.split(',')

print(shoplist)

"""
根据你购买的产品把购物清单中相应的物品删除掉，并得到新的购物清单，
由于这里我用了for循环所以得到的是字符串，不能用del通过索引删除，只能用remove通过你的元素来删除
"""

food = input("Which food you have bought?")

for j in shoplist:
    if j == food:
        shoplist.remove(j)
print(shoplist)
