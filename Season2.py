import random

print("Title:-------Hello world&Hello Python-------")
print("Here is a game:guessNumber 2.0")
#实现当输入错误数据时，提示正确数据的大小关系。
#实现多次猜测的机会。
#实现对于正确数据的随机性
#使用and语句实现多条件限制
guess=random.randint(1,10)
temp=int(input("input a number : "))
wrongNumber=0
while (temp != guess)and(wrongNumber<4):   
     if guess < temp:
          print("Big")
     else:
          print("Small")
     temp=int(input("input a number"))
     wrongNumber=wrongNumber+1
if guess==temp:
     print("Ok")
else:
     print("The maximum number of errors has been reached")
print("The game is end")

#------Tips 1------
#type(parameter)查看给定参数的数据类型
#isinstance(parameter1,parameter2)对比给定两个参数的数据类型的相似性，返回值类型Boolen
#int(parameter)将给定的参数转换为int型数据，并将其返回。
#str()，float()返回字符串类型和字符类型。

#------Tips 2------
# +（加）、-（减）、*（乘）、/（除）、//（下除，比如3//4==1）、**（求幂）、%（求余）
#基本算术运算符的优先级为：先加减后乘除。
#对于幂操作，幂运算操作大于其左侧数据小于其右侧数据，比如 -2 ** 4=-16

#------Tips 3------
#比较操作符<、<=、>、>=、==、!=
#逻辑操作符：and、or、not

#对于整体的优先级:
# **
# 正负号
# *、/、//
# =、-
# <、<=、>、>=、==、!=
# not and or
