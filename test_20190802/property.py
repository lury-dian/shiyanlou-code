#! /usr/bin/env python3
class Account(object):
    """
    账号类
    amount是美元金额
    这个类就是你可以看到你的账户里面有多少美元，换算成人民币又是多少
    """
    def __init__(self, rate):
        self.__amt=0
        self.rate = rate
        """
        这里的__amt不想要别人访问，所以前面加了下划线是私有的，默认是0
        外面有对他进行赋值
        """

    @property
    def amount(self):
        """账号余额（美元）"""
        return self.__amt

    @property
    def cny(self):
        """账号余额（人民币）"""
        return self.__amt * self.rate

    @amount.setter
    def amount(self,value):
        if value<0:
            print("Sorry, no negative amount in the account.")
            return
        self.__amt=value
        """这里可以看到如果你的金额小于0，会直接返回美元的值
        装饰器不知道什么意思
        但是根据结果应该是直接返回账户实际余额，如果得到的值是负数的话
        """

if __name__=='__main__':
    acc=Account(rate=6.6)
    acc.amount=-20
    print("Dollar amount: ",acc.amount)
    print("In CNY: ",acc.cny)
    acc.amount=-100
    print("Dollar amount: ",acc.amount)
