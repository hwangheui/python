# id=input("아이디 입력:")
# pw=input("비밀번호 입력:")

# print(f"아이디: {id} / 비밀번호:{pw}")
# print(type(id), type(pw))

# 더하기 프로그램
# num1= int(input("첫번째 숫자 입력"))
# num2= int(input("두번째 숫자 입력:"))

# print(f"{num1} + {num2}= {num1+num2}")
# print(type(num1), type(num2))

#문자열 
# fruit1 ="수박"
# fruit2 ="딸기"

# print( fruit1+ fruit2)
# #print(fruit1-fruit2) #불가능
# print(fruit1*3)
# print(fruit)



# s1='ABCDEFGHIJKLNMOPQRXTUVWXYZ'
# s2='abcdefghijklnmopqrxtuvwxyz'

# name=s1[7]+s2[-4]+s2[0]+s2[-14]+s2[6]+s2[7]+s2[4]+s2[-6]+s2[8]
# print(name)
# print(name[:5])
# print(name[-4:])
text="\t\"There is no one\n who loves pain itself,\n who seeks after it\n and wants to have it,\n simply because it is pain...\"" 
print(text.count('a')) #특정문자의 갯수 반환
print(text.upper()) # 문자열을 대문지로 변환
print(text.replace('who','that')) #문자열에서 who를 that으로치환
print(len(text)) # 문장의 길이 반환
print(text.split(',')) #해당 문자레소 문장분

