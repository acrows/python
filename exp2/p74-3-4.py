# p74  3.4
# 输入字符串
url = "https://www.tsinghua.edu.cn/"

# ① 输出第1个字符
print(url[0])

# ② 提取"www"子串 (正向切片)
substring_forward = url[8:11]
print(substring_forward)

# ② 提取"www"子串 (反向切片)
substring_backward = url[-15:-12]
print(substring_backward)

# ③ 输出字符串中"edu"子串出现的位置
edu_index = url.find("edu")
print(edu_index)

# ④ 输出字符串中字母t出现的次数
t_count = url.count("t")
print(t_count)

# ⑤ 将字符串中所有的“.”替换为“-”
replaced_url = url.replace(".", "-")
print(replaced_url)

# ⑥ 将字符串中的字母全变为大写字母
uppercase_url = url.upper()
print(uppercase_url)

# ⑦ 输出字符串的总字符个数
length = len(url)
print(length)
