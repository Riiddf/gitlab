# -*- coding: utf-8 -*-
#2017.3.20 16：45 Python代码小练习---小明的成绩提升
print('计算成绩变化百分点')
s1=int(input('请输入你的第一次成绩：'))
s2=int(input('请输入你的第一次成绩：'))
r = (s2-s1)/s1*100
if s1<s2:
     print('小明的成绩提升了%.1f%%' % (r))
elif s1==s2:
     print('小明的成绩没有提升')
else:
     print('小明的成绩下滑了%.1f%%' % (-r))