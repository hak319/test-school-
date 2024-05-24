# 성적을 저장할 리스트 생성
test1 = []

# 학생 수
num_students = 5

# 학생 수 만큼 반복하여 성적 입력 받기
for i in range(num_students):
    grade = float(input(f"성적을 입력하세요: "))
    test1.append(grade)

# 성적의 평균 계산
average_grade = sum(test1) / len(test1)

# 최대, 최소 성적 계산
max_grade = max(test1)
min_grade = min(test1)

# 80점 이상 성적을 받은 학생의 수 계산
num_students_above_80 = len([grade for grade in test1 if grade >= 80])

# 결과 출력
print("성적 평균 = ", average_grade)
print("최대점수 = ", max_grade)
print("최소점수 = ", min_grade)
print("80점 이상 =", num_students_above_80)