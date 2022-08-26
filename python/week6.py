### 튜플
## 튜플 생성
# t1 = (1, 2, 3)
# t2 = 'a', 'b', 'c'
# print(t1)
# print(t2)
# print(t1+t2) #반복
# print(t1*3) #병합
# print(t1[2])

### 튜플 /딕셔너리
# 리스트 복사
# l1 =[1, 2, 3]
# #12 = l1 #리스트의 링크(주소)를 l2 연결
# l2 = l1[:]     #l1 리스트의 값 전체를 l2라스트에 복사
# print(l1)
# print(12)
# l2.append(4)
# print(l1)
# print(l2)
# print(l1 == l2) #비교연산자 ==는 갑을 비교
# print(l1 is l2) #is 연산자 : 같은 객체이지 비교

# t1 =(1, 2, 3)
# t2 = t1[:]  # tuple(t1)
# print(t1)
# print(t2)
# print(t1 == t2)
# print( t1 is t2)

### 딕셔너리 생성
dic = {'이름':'황희', 'age':'17', 'school':'중앙고'}
print(dic, type(dic))
print(dic['이름'])
#딕셔너리 추가 
# dic['class'] = 3
# dic['키'] =175.123
# print(dic)
# #딕셔너리 수정 
# dic['age'] = 27
# print(dic)
# #딕셔너리 삭제
# del dic['키']
# print(dic)

##딕셔너리 합수(메소드)
print(dic.keys()) #keys 들만 묶어서 반환
print(dic.values()) #valuese들만 묶어소 반환
print(dic.items())  #key와 values가 쌍으로 묶어서 반환
print(dic.get('age')) #'key'에 해당하는 values값을 반환
print(dic.update({'class':3, '키':179, 'age':19})) #'key'에 값에 해당하는 values 값을 반환
print(dic)
print(dic, type(dic)) #딕셔너리 d의 모든 item삭제


#딕셔너리 실습
fruits = {'apple':'500','banana':'2500', 'mango':'2000'}
print("망고는 1개당 %s원입니다. " %fruits['mango'])





