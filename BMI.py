height = input('請輸入您的身高:')
weight = input('請輸入您的體重:')
height = float(height)
weight = float(weight)
height2 = height * 0.01
bmi = weight / (height2 * height2)
print('您的BMI為', bmi)
if bmi < 18.5 :
    print('過瘦')
if bmi >= 18.5 and bmi< 24 :
    print('標準')
if bmi >=24 and bmi < 27:
    print('過重')
if bmi >=27 and bmi < 30:
    print('輕度肥胖')
if bmi >=30 and bmi < 35:
    print('中度肥胖')
if bmi > 35:
    print('重度肥胖')