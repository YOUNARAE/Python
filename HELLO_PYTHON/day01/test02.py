# 첫번째수를 넣으세요 1
# 두번째수를 넣으세요 10
# 1에서 10까지 합은 55입니다.


a = input("첫번째수를 넣으세요")
b = input("두번째수를 넣으세요")
aa = int(a)
bb = int(b)

sum = 0
for i in range(aa,bb+1):
    sum += i
    
print("{}에서 {}까지 합은 {}입니다.".format(aa,bb,sum))
