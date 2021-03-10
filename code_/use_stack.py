# coding: utf-8
from pythonds.basic.stack import Stack


# 利用栈实现括号是否匹配的判断
# def parsechecker(onestring):
#     s = Stack()
#     matcher = {
#         "(":")",
#         "[":"]",
#         "{":"}",
#     }
#     for i in range(len(onestring)):
#         if onestring[i] in "([{":
#             s.push(onestring[i])
#         elif onestring[i] in ")]}":
#             # p = s.pop()
#             p = s.peek()
#             if matcher[p] == onestring[i]:
#                 s.pop()
#     if s.size() == 0:
#         return True
#     else:
#         return False
#
#
# print(parsechecker("(([hhh))]"))


# 利用栈实现十进制转化为二进制
def divideby2(octnumber):
    s = Stack()

    while octnumber > 0:
        yunumber = octnumber % 2
        octnumber = octnumber // 2

        print("octnumber===", octnumber)
        print("yunumber===", yunumber)
        s.push(yunumber)

    binstring = ""
    while not s.isEmpty():
        binstring = binstring + str(s.pop())
    return binstring


# print(divideby2(35))


# 十进制转换为十六以下的任意进制
# def baseConverter(octnumber, base):
#     s = Stack()
#     digits = "0123456789ABCDEF"
#     while octnumber > 0:
#         yunumber = octnumber % base
#         octnumber = octnumber // base
#
#         print("octnumber===", octnumber)
#         print("yunumber===", yunumber)
#         s.push(yunumber)
#
#     binstring = ""
#     while not s.isEmpty():
#         binstring = binstring + digits[s.pop()]
#     return binstring
#
#
# print(baseConverter(25,16))

import turtle

t = turtle.Turtle()
t.pencolor('red')
t.pensize(3)
for i in range(5):
    t.forward(100)
    t.right(144)
t.hideturtle()
turtle.done()






























