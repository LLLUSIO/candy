num_01 = int(input("请输入1号小朋友的糖果数: "))
num_02 = int(input("请输入2号小朋友的糖果数: "))
num_03 = int(input("请输入3号小朋友的糖果数: "))
num_04 = int(input("请输入4号小朋友的糖果数: "))
num_05 = int(input("请输入5号小朋友的糖果数: "))

#一号小朋友分为糖果后，每位小朋友糖果的变化情况
num_01 = int(num_01/3)
num_05 = num_01 + num_05
num_02 = num_01 + num_02

#二号小朋友分为糖果后，每位小朋友糖果的变化情况
num_02 = int(num_02/3)
num_01 = num_02 + num_01
num_03 = num_02 + num_03

#三号小朋友分为糖果后，每位小朋友糖果的变化情况
num_03 = int(num_03/3)
num_02 = num_02 + num_03
num_04 = num_04 + num_03

#四号小朋友分为糖果后，每位小朋友糖果的变化情况
num_04 = int(num_04/3)
num_03 = num_04 + num_03
num_05 = num_04 + num_05

#五号小朋友分为糖果后，每位小朋友糖果的变化情况
num_05 = int(num_05/3)
num_04 = num_04 + num_05
num_01 = num_01 + num_05
print(num_01,num_02,num_03,num_04,num_05)

#1.python中的输入都是字符串，直接使用运算符计算会出错，需要先转换成整数
#2.python中直接使用除法，结果会是小数，如果需要的是商，可以通过int或者//运算符来达到取整数的目的。

# for i in range(1,5):
#     num_i=int(input("请输入第i位小朋友的糖果数:"))
# for i in range(1,5):
#     num_i=int(num_i/3)
#     num_i+1=int(num_i+num_i+1)
#     num_i-1=int(num_i+num_i-1)
# for i in range(1, 5):
#      print(num_i)