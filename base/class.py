class MyClass:
    """一个简单的类实例"""
    i = 12345
    def __init__(self):
        self.data = ['1']

    def f(self):
        return 'hello world'
 
# 实例化类
x = MyClass()
 
# 访问类的属性和方法
print("MyClass 类的属性 data 为：", x.data)
print("MyClass 类的方法 f 输出为：", x.f())