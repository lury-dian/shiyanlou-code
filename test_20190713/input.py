
#计算平均值
#! /usr/bin/env python3
n = int(input("how many numbers do you want"))
sum = 0
count = 0
print("Plase input numbers: ")
while count < n:
        number = float(input())
            sum = sum + number
                count += 1
                average = sum/n
                print("N={},Sum ={}".format(n,sum))
                print("Average=={:.2f}".format(average))


#根据总天数计算月数和天数
#! /usr/bin/env python3
days = int(input("Enter days: "))
print("Months = {} Days = {}".format(*divmod(days,30)))
#divmod(num1,num2) can return tuple,this tuple contains two values, one is num1//num2, other one is num1%num2, then use * to unpacking this tuple.


#将摄氏度转换成华氏度
#! /usr/bin/env python3
fahrenheit=0
print("Fahrenheit Celsius")
while fahrenheit <= 250:
        celsius = (fahrenheit - 32)/1.8
            print("{:5d} {:7.2f}".format(fahrenheit,celsius))
                fahrenheit += 25
