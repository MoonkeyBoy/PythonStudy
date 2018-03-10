#爬虫的学习：


#----Python如何访问互联网------
'''
通过urllib 包访问
'''

#----Python如何获得网页图片------
'''
import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/200/300")
cat_img = response.read()

with open('cat_200_300.jpg', 'wb') as f:
    f.write(cat_img)
'''
