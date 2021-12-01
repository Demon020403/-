'''通过自定义函数，实现RPSLS游戏，即用户通过键盘输入任意一个选择（石头/剪刀/布/蜥蜴/史波克），
计算机自动生成一个随机选择，根据RPSLS规则，产生最终的结果，土木一班马镖'''
import random #导入random模块
answer=random.randint(0,4) #利用randint方法产生随机整数
print("欢迎开始rpsls游戏")
print("我们分别用0，1，2，3，4对应石头/剪刀/布/蜥蜴/史波克")
print("石头=0")
print("史波克=1")
print("布=2")
print("蜥蜴=3")
print("剪刀=4")
a=input("请输入你的选择对应的数字")
def rpsls (a,answer):
    h=int(a)-int(answer)
    if h==1:
        print("你的选择是"+str(a))
        print("机器的选择是"+str(answer))
        print("你赢了")
    elif h==2:
        print("你的选择是"+str(a))
        print("机器的选择是"+str(answer))
        print("你赢了")
    elif h==-3:
        print("你的选择是"+str(a))
        print("机器的选择是"+str(answer))
        print("你赢了")
    elif h==-4:
        print("你的选择是"+str(a))
        print("机器的选择是"+str(answer))
        print("你赢了")
    elif h==0:
        print("你的选择是"+str(a))
        print("机器的选择是"+str(answer))
        print("你们平局了")
    else:
        print("你的选择是"+str(a))
        print("机器的选择是"+str(answer))
        print("机器赢了")
    if int(a)==1:
        rpsls(a,answer)
    elif int(a)==2:
        rpsls(a,answer)
    elif int(a)==0:
        rpsls(a,answer)
    elif int(a)==3:
        rpsls(a,answer)
    elif int(a)==4:
        rpsls(a,answer)
    else:
        print("请输入0-4之间的数字")