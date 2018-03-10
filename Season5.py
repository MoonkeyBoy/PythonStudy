#字符串的简洁使用
#http://www.runoob.com/python3/python3-string.html

#一个重要的函数：format()
#位置参数
print("{0} love {1}".format("1","2"))
#关键字参数
print("{a} love {b}".format(a="1",b="2"))
#两者同时使用时，位置参数需要在关键字参数之前
print("{0} love {b}".format("1",b="2"))


#Python字符串格式化
#http://www.runoob.com/python3/python3-string.html


#------------Tips -------------
'''
列表、元组和字符串的共同点，此处统称序列
都可以通过索引得到每一个元素
默认索引值总是从0开始
可以通过分片的方法得到一个范围内的元素的集合
有很多共同的操作符（重复操作符、拼接操作符、成员关系操作符）
'''
#序列有很多共有的函数，比如：max()、min()、len()
