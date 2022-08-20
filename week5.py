#김밥만들기
# item0 = '김'
# item1 = '밥'
# item3 ='단무지'
# item4 = '계란'
# item5 = '시금치'

# print( item0, item1, item3, item4, item5)

# # items = ['김', '밥', '단무지', '계란', '시금치']
# # print(items)

# students = ['이황희', '김강빈', '김민건', '유건우', '강민준']
# # print(students)
# # print(students[0])
# # print(students[1])
# print(students[2:4])
# print(students*2)
# print(students+students)

# score = [100, 85, 80, 70, 100]
# text = 'coding'

##리스트 활용 함수
# print(max(score)) # 최대값
# print(min(score)) #최소값
# print(len(score))#len  길이
# print(sum(score)) #리스트안에 총합
# print(text)
# print(list(text))#list 리스트로 변환

# ### 리스트 메소드
# score.append(85) #리스트 마지막 값 추가
# print(score) 
# score.insert(3 ,75) # 리스트 n번째 위치에 값 추가
# print(score)
# # score.pop() #리스트 마지막 값 삭제
# # print(score)
# score.remove(100) #특정 값 삭제 (앞에서 부터 검색)
# print(score)
# score.extend(students) #리스트 병합
# print(score)

# print(score.index(70)) #리스트에소 해당 값의 인덱스 반환
# print(score.count(100)) # 리스트에서 해당 값의 개수 반환

#리스트 정렬
# score.reverse() #역순 정렬
# print(score)
# score.sort() # 오름차순 정렬 (작은수에서 큰수)
# print(score)
# score.sort(reverse=True) #내림차순 정렬 (큰수에서 작은 수)
# print(score)
 
 
# 학생 명부 만들기

student1 = ['이황희', '남', 27, '4반', '01055269203']
student2 = ['산희', '남', 10, '7반', "010555555555"]

#중첩 리스트
student_list = [student1, student2]
print(student_list)
print(student_list[0][0])
print(student_list[1][4])











