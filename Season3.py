#传统的打飞机游戏制作的思路
#interval变量是设置对于飞机诞生的时间间隔
'''
加载背景音乐
播放背景音乐（设置单曲循环）
我方飞机诞生
interval = 0

while True:
    if 用户是否点击了关闭按钮:
        退出程序
    
    interval += 1
    if interval == 50:
        interval = 0
        小飞机诞生

    小飞机移动一个位置
    屏幕刷新
    
    if 用户鼠标产生移动:
        我方飞机中心位置 = 用户鼠标位置
        屏幕刷新
        
    if 我方飞机与小飞机发生肢体冲突:
        我方挂，播放撞机音乐
        修改我方飞机图案
        打印“Game over”
        停止背景音乐，最好淡出
'''

#下面简单的看下这个问题：按照100分制，90分以上成绩为A，80到90为B，60到80为C，60以下为D，写一个程序，当用户输入分数，自动转换为ABCD的形式打印。
#这里有三个程序
#----程序1----
'''
score = int(input('请输入一个分数：'))
if 100 >= score >= 90:
    print('A')
if 90 > score >= 80:
    print('B')
if 80 > score >= 60:
    print('C')
if 60 > score >= 0:
    print('D')
if score < 0 or score > 100:
    print('输入错误！')

'''
#----程序2----
'''
score = int(input('请输入您的分数：'))
if 100 >= score >= 90:
    print('A')
else:
    if 90 > score >= 80:
        print('B')
    else:
        if 80 > score >= 60:
            print('C')
        else:
            if 60 > score >= 0:
                print('D')
            else:
                print('输入错误！')
'''
#----程序3----
#elif 是else if 的缩写
'''
score = int(input('请输入一个分数：'))
if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
    print('B')
elif 80 > score >= 60:
    print('C')
elif 60 > score >= 0:
    print('D')
else:
    print('输入错误！')
'''
#比较一下，其程序的效率第一个相比第二、三个差。


#-------Tips 1------
#悬挂else:定义
'''
if ( hi > 2 )
	if( hi > 7 )
		printf(“好棒！好棒！”);
else
	printf(“切~”);
'''
#对于上面的程序段，C语言规定else所对应的if是第一个if 而不是第二个，但是在Python中会根据缩进规则选择所匹配的if语句
#-------Tips 2------
#条件表达式（三元操作符）
'''
if x < y:
	small = x
else:
	small = y
例子可以改进为：
small = x if x < y else y
'''

#-------Tips 3------
#断言（assert）
#assert这个关键字我们称之为“断言”，当这个关键字后边的条件为假的时候，程序自动崩溃并抛出AssertionError的异常。
#举例
'''
>>> assert 3>5
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    assert 3>5
AssertionError
'''


#-------Tips 8------
'''
for 目标 in 表达式:
    循环体
'''


#-------Tips 9------
#range()
'''
语法：range( [start] ,stop,[step=1] )
这个BIF有三个参数，其中用中括号括起来的两个表示这两个参数是可选的。
step=1表示第三个参数的值默认值是1。
range这个BIF的作用是生成一个从start参数的值开始到stop参数的值结束的数字序列。
'''
#-------Tips 10------
#循环中break和continue的使用和C语言相同










