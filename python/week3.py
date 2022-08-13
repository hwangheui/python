 # 변수
# print('10**2')
# name="이황희"
# age=17
# _height=175

# print(name)
# print(age)
# print(_height)




# 변수의 연산
# time=10
# # print(time)
# # time=11
# print(time)
# time=time+1
# time+= 1
# print(time)

#비교연산자
# a=10
# b=20
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

# print(a<b and a==10)
# print(a>b and a==10)
# print(a>b and a!=10)

# print(a>b or a==10)
# print(a<b or a==10)
# print(a>b or a!=10)

# print(not a>b)
# print(not a<b)
# print(not a==10)


# 포멧팅
print('10**2')
name="이황희"
age=17
height=175.123
print("이름:",name, "나이:" ,age, "키:",height) # 텍스트, 변수
print("이름: %s, 나이: %d, 키: %.1f" %(name, age, height)) #포멧기호
print("이름:{}, 나이:{}, 키:{:.2f}".format(name, age, height))#포멧함수
print("이름:{2}, 나이:{0}, 키:{1:.2f}".format(name, age, height)) #인덱스 활용
print(f"이름: {name}, 나이: {age}, 키: {height:.2f}") #f-string


