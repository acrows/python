def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# 测试三条边
print("请输入三条边:")
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

result = is_triangle(a, b, c)
if result:
    print("可以构成三角形")
else:
    print("无法构成三角形")