# ### 반복문 for

friends = ['황희', '피카츄', '꼬부기']

while index < 3:
    print(friends[i])
    i += 1

# # #for 변수 in 배열:
# # #for 변수 in 순서가 있는 자료형:

# # # for f in friends:  # 변수 정의 안해도 됨
# # #     print(f) 


# # ### 딕셔너리 x for
# # stdnt = {'name':'황희', 'school':'중앙고', '반':'4반'}
# # # print(stdnt['name'])
# # for i in stdnt: # 딕셔너리는 key 값이 전달된다
# #     print(stdnt[i]) # values 출력 방법
    
# ### continue

# score ={'수학':100, '영어':80, '국어':80,
#         '사회':70, '과학':90, '체육':70}

# for i in score:
    
#     # if score[i] >= 80:
#     #     print(f"축하합니다. {i} 패스했습니다.")
#     if score[i] < 80:
#         continue
#     else:
#         print(f"축하합니다. {i} 패스했습니다.")
    
### range() 함수
# r1 = list(range(10)) #range(끝 값 +1)
# print(r1)

# r2 = list(range(3,10)) #range(시작 값, 끝 값+1) #시작값부터 끝 값까지 출력
# print(r2)

# r3 = list(range(3, 11, 2)) #range(시작 값, 끝값+1, 간격)
# print(r3)

### for x range()
# for i in range(1, 11): #1부터 11 까지 반복
#     print(i, end='') # end 줄바꿈안하고 
    
# for i in range(11): #0부터 10까지 반복
#    print(i, end='')
   
# for i in range(1, 101, 2):
#     print(i, end=' ')
    
    
# i = int(input('숫자를 입력해주세요:'))

# for h in range(1, i+1):
#     print(h, end=' ')

# i = int(input('숫자를 입력하세요:'))
# H = int(input('숫자를 입력하세요:'))

# for num in range(i, H+1):
#     print(num, end= ' ')
    

        
    

#숙제
#(1부터 100 까지 3의 배수 출력 10개씩 줄 바꿔서 출력)

for i in range(3, 100, 3):
    print(i, end=' ')
    if i%30 ==0:
        print()

    





 