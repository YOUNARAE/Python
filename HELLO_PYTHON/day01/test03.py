# 홀/짝을 넣으세요 홀
# 나:홀
# 컴:짝
# 결과:졌음
import random

mine = input("홀/짝을 넣으세요")
com = ""
result =""

rnd = random.random()

if rnd >0.5 :
    com = "홀"
else:
    com = "짝" 
    
if mine == com  :
    result = "이김"
else:
    result = "짐" 

print("mine",mine)
print("com",com)
print("result",result)