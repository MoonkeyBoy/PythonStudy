print("Title:-------Hello world&Hello Python-------")

print("\n")
print("Codes: print(\"Hello \"+\"World \")")
print("Hello "+"World ")
print("\n")

print("Codes: Print the print(\"Hello world \" * 2)")
print("Hello world" * 2)
print("\n")

print("Codes: print(3+5)")
print(3+5)
print("\n")
#------Tips 1------
#Codes :print("Hello world" + 2) is wrong.


print("Here is a game:guessNumber 1.0")
temp=input("input a number")#input()、int() are BIF(Built-in functions),可以通过Python的shell命令dir(__builtins__)查看所有的BIF,具体的命令通过help(xx)来查看。
#input功能：获得键盘输入
guess =int (temp)#强制转换成int
if guess==8:#这里有个冒号
     print("Ok")
else:#这里也有个冒号
     print("No Ok")
#Python中if else 结构是通过冒号和Tab缩进键实现的，所有Python中Tab间很关键。
print("The game is end")


    
#------Tips 2------
#原始字符串的使用非常简单，只需要在字符串前边加一个英文字母r即可：
#str = r'C:\Program Files\Python\Help'
#如果希望得到一个跨越多行的字符串，例如：
#Hello World
#Hello Python
#Hello Xuheng
#这我们就需要使用到三重引号字符串！(单引号、双引号都可以)
#'''
# Hello World
# Hello Python
# Hello Xuheng
#'''


