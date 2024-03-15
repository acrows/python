#p74 3.3
print("请输入三门成绩:")
chinese = float(input("语文="))
math = float(input("数学="))
english = float(input("英语="))
total = chinese + math + english
print("总分为%.2f" % total)
print("平均分为%d" % (total / 3))
print("最高分为%.2f" % (max([chinese, math, english])))
print("最低分为%.2f" % (min([chinese, math, english])))