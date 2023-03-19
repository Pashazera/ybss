"""
    Author: Pashazera
    Time  : 2023/3/8 21:48
    File  : t.py
    describe :
"""
import json
import os
import random
import sys
import time

import pandas as pd
import re
import demjson

j = {"code":"200","msg":"成功","data":"{\"code\":\"200\",\"msg\":\"成功\",\"data\":\"{\\\"total\\\":1,\\\"resultData\\\":[{\\\"applyType\\\":1003,\\\"acceptDate\\\":\\\"2019-11-22 09:02:05.0\\\",\\\"corpAddr\\\":\\\"江苏省南京市中山北路406-3号\\\",\\\"ecoType\\\":1407,\\\"licNo\\\":\\\"1132010460\\\",\\\"corpName\\\":\\\"江苏中烟工业有限责任公司\\\",\\\"biId\\\":\\\"913200001347645408\\\",\\\"managerName\\\":\\\"曾献兵\\\",\\\"resultStatus\\\":-9999,\\\"decideDate\\\":\\\"2019-11-22 12:26:13.0\\\",\\\"idcard\\\":\\\"432401196510244070\\\",\\\"validateEnd\\\":\\\"2019-12-29\\\",\\\"licIssuingOrg\\\":\\\"国家烟草专卖局\\\",\\\"validateStart\\\":\\\"2014-12-29\\\",\\\"busiScope\\\":\\\"卷烟生产销售;卷烟纸、滤嘴棒、烟用丝束购进;雪茄烟生产销售;烟草专用机械购进;烟叶、烟丝、复烤烟叶购进;\\\"}],\\\"resultHead\\\":{\\\"count\\\":1,\\\"message\\\":\\\"查询成功！\\\",\\\"status\\\":\\\"200\\\"}}\"}"}


a = j["data"]
str = demjson.decode(a)
s = str["data"]
s = demjson.decode(s)
s = s["resultData"]

#print(pd.DataFrame(s))




def getJson(dict_json):
    temp = dict_json["data"]
    a = demjson.decode(temp)
    temp = a["data"]
    a = demjson.decode(temp)
    res = a["resultData"]

    return res


def Fibonacci(n):
    temp = 0
    left = 1
    right = 1
    list = []
    list.append(left)

    if n <= 1 :
        list.pop()
        pass

    else:
        list.append(right)
        for i in range(n-2):
           temp = right
           right = right + left
           left = temp
           list.append(right)
    print("Fibonacci %d:" %(n))
    print(list)



def Perfect_umber(n):
    list = []
    temp = []
    for k in range(2,n+1):
        for i in range(1,k):
            if k%i == 0:
                temp.append(i)
        sum = 0
        for t in temp:
            sum = sum + t

        if k == sum:

            list.append(k)
        temp.clear()

    print("Perfect_umber:")
    print(list)

def prime_number(n):
    list = []
    temp = True
    for k in range(2,n+1):
        for i in range(2,k):
            if k%i == 0:
                temp = False
        if temp == True:
            list.append(k)
        temp = True

    print("prime number:")
    print(list)

str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1)) # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or')) # 8
print(str1.find('shit')) # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())

a, b = 5, 10
print(f'{a} * {b} = {a * b}')
print(f"{a}+{b} =  {a*b}")


f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
print(f.__len__())
print(len(f))

# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

set1.add(4)
set1.add(5)
print("set1=",set1)
set2.update([11, 12])
print("set2=",set2)
set2.discard(5)
set2.remove(1)
print("set2=",set2)
if 4 in set2:
    set2.remove(4)
print(set1, set2)
print(set3.pop())
print(set3)

s = "asdfg"
print(s[1:])

def run_l():
    """
    跑马灯
    :return:
    """
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


def build_cheak_data(code_len = 6):
    """
    返回一个验证码
    :param code_len:验证码的长度
    :return:验证码
    """
    n = code_len
    if n < 6:
        print("你的验证码小于%d"%n)
    else:
        num_chars = '0123456789'
        small_str = "abcdefghijklmnopqrstuvwxyz"
        big_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        small_str_num  = random.randint(1,n-2)
        num = random.randint(1,n-small_str_num-1)
        big_str_num = n -num - small_str_num
        n_code = ""
        s_code = ""
        b_code = ''
        code = ""
        for _ in range(num):
            k = random.randint(0,num_chars.__len__()-1)
            n_code += num_chars[k]
        for _ in range(small_str_num):
            k = random.randint(0,small_str.__len__()-1)
            s_code += small_str[k]
        for _ in range(big_str_num):
            k = random.randint(0,len(big_str)-1)
            b_code += big_str[k]
        code = n_code + s_code + b_code
        print(n_code,s_code,b_code)
        code = list(code)
        random.shuffle(code)
        print("".join(code))
        code = "".join(code)
        return code

def get_suffix(filename ):
    """
    返回文件的后缀名
    :param filename: 文件名
    :return: 后缀名
    """
    pos = filename
    if 0 < pos.find(".") < len(filename) :
        return filename[pos.find(".")+1:]
    else:
        return ""

class Person():

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    """
    @property装饰器来创建只读属性，
    @property装饰器会将方法转换为相同名称的只读属性,可以与所定义的属性配合使用，这样可以防止属性被修改。
    """
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    @name.setter
    def name(self,name):
        self._name = name



    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)
    def show(self):
        print(self._name,self._age)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    #person.name = '白元芳'  # AttributeError: can't set attribute
    person.name = "ducheng"
    person.show()
    print(person.name)



if __name__ == '__main__':
    main()

