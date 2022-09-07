### 반복문 while
# num = 0 

# while num < 10:
#     num += 1
#     print(f"{num}번 뛰었습니다.")
# count = 0

# while count < 10:
#     count += 1
#     print(f"{count}번 찍었습니다.")
# else:
#     print("나무가 넘어간다")


# members=['Tommy', 'marry', 'Hwangheui']
# count = 3
# while count > 0:
    
#     ID= (input('아이디 입력:'))
    
#     if ID in members:
#         print('로그인 성공')
#         break
#     # elif (len(ID)) >= 5:
#     # members.append(ID)
#     # print(f"당신의 아이디는 {ID} 입니다")
#     else:
#         print("로그인 실패")
#     count -= 1  #count = count - 1

# members=['Tommy', 'marry', 'Hwangheui']

# while True:
    
#     ID= (input('아이디 입력:'))
    
#     if ID in members:
#         print('로그인 성공')
#         break
    # elif (len(ID)) >= 5:
    # members.append(ID)
    # print(f"당신의 아이디는 {ID} 입니다")
    # else:
    #     print("로그인 실패")

### * 출력
# star = 0
# while True:
#     star += 1
    
#     if star > 5:
#         break 
#     else: 
#         print('*' * star)




school = []
while True: 
    reply = input("학교에 가면?") 
    
    if reply not in school:
        school.append(reply)
        print(f"{reply}(이)가 있고")
    # elif reply in school:
    else:
        print("탈락")
        break
    
    
    

        
        
    