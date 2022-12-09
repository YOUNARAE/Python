# 가위/바위/보을 넣으세요 가위
# 나:가위
# 컴:가위
# 결과:비김
import random

mine = input("가위/바위/보을 넣으세요")
com = ""
result =""

rnd = random.random()

if rnd >0.66 :
    com = "가위"
elif rnd >0.33 :
    com = "바위"
else:
    com = "보" 
    
if com == "가위" and mine == "가위" :   result ="비김"
if com == "가위" and mine == "바위" :   result ="이김"
if com == "가위" and mine == "보" :   result ="짐"

if com == "바위" and mine == "가위" :   result ="짐"
if com == "바위" and mine == "바위" :   result ="비김"
if com == "바위" and mine == "보" :   result ="이김"

if com == "보" and mine == "가위" :   result ="이김"
if com == "보" and mine == "바위" :   result ="짐"
if com == "보" and mine == "보" :   result ="비김"

print("mine",mine)
print("com",com)
print("result",result)















