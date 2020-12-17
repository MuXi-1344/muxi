"""
一、函数的定义以及函数的调用
函数代码块以 def 关键词开头，后接函数名称和圆括号 ()
   冒号起始
   注意缩进
   圆括号中定义参数
   函数说明——文档字符串
return[表达式]结束函数
   选择性地返回一个值给调用方
   不带表达式的return或者不写return函数，相当于返回None

#函数的定义
#def func1(a,b,c):
    #快捷键ctrl+d：复制一行
    #print("打印函数a =", a)
    #print("打印函数b =", b)
    #print("打印函数c =", c)
#函数调用
#func1(2,3,4)

#return使用
#def func2(a,b,c):
    #return a+b+c
    #return
#函数调用
#print(func2(3,4,6))
"""

"""
二、函数的默认参数
默认参数：默认参数在定义函数的时候使用k=v的形式定义。
        调用函数时，如果没有传参，则会使用默认参数.
        如果传递了参数时就会使用传递的参数
def func3(a=2):
    print("打印a的值为", a)
    #print("打印b的值为", b)
    #print("打印c的值为", c)
#函数的调用
func3(5)
"""

"""
三、函数的关键字参数
   在调用函数的时候，使用k=v的方式进行传参
   在函数调用/定义中，关键字参数必须跟随在位置参数的后面
def func4(a,b,c):
    print("a的值为",a)
    print("b的值为",b)
    print("c的值为",c)  
func4(10,c=23,b=12)
"""

"""
四、特殊函数（了解用法即可）
     *:仅限关键字参数，在【仅限关键字参数】形参前放置一个*
def func5(a,b,c,*,d):
    print("a的值为", a)
    print("b的值为", b)
    print("c的值为", c)
    print("d的值为", d)
func5(5,10,34,d=8)
"""

"""
五、Lambda表达式
func6 = lambda x:x*2
print(func6(3)) 
"""

