# -*- coding: utf-8 -*-

height = float(input('请输入您的身高（米）：'))
weight = float(input('请输入您的体重(千克)：'))
bmi = (weight)/(height*height)
if BMI<0:
    print('数据有误')
elif bmi<=18.5:
    print('BMI=%.2f'%bmi,'你的体重过轻')
elif bmi>=18.5 and bmi<25:
    print('BMI=%.2f'%bmi,'你的体重正常')
elif  bmi>=25 and bmi<28:
    print('BMI= %.2f'%bmi,'你的体重过重')
elif  bmi>=28 and bmi<32:
    print('BMI=%.2f'%bmi,'你的体重肥胖')
else:
    print('BMI=%.2f'%bmi,'你的体重严重肥胖')
