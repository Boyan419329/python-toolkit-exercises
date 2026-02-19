#由键盘接受一个年龄
age = input("请您输入年龄：")#接收键盘输入的内容并且赋值给变量age
print("年龄为:"+ age)
print(type(age))
#将接收到的年龄进行加10计算，并赋值给变量age_new

print("计算后的年龄为："+ age)#默认使用input函数接收的值为str字符串类型，如果要进行运算，需要进行类型转换
age_new= int(age)+ 10
print("计算后的年龄为:"+ str(age_new))
