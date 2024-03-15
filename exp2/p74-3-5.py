# p74 3.5
# 输入整数
num = int(input("请输入一个1~7之间的整数: "))

# 判断并输出对应的中文星期名称
if num == 1:
    print("星期一")
elif num == 2:
    print("星期二")
elif num == 3:
    print("星期三")
elif num == 4:
    print("星期四")
elif num == 5:
    print("星期五")
elif num == 6:
    print("星期六")
elif num == 7:
    print("星期日")
else:
    print("输入无效，请输入1~7之间的整数。")
