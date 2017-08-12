def out():
    a = 1
    def inner():
        print a
        #此处调用的a，不属于全局变量，不属于函数代码块内部变量，而是外层函数的局部变量，
        #
        #闭包是指可以包含自由（未绑定到特定对象）变量的代码块；这些变量不是在这个
        #代码块内或者任何全局上下文中定义的，而是在定义代码块的环境中定义（局部变量）。
        print "I'm inner"
    return inner

f = out()   #此时的 f 相当于inner()函数
f()         # f()相当于对inner() 的调用
