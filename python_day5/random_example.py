import random

random_number = random.randint(1, 45)
print(random_number)

# 랜덤한 사람을 뽑기?
students = ['김지민', '유수진', '이은선', '류용윤', '유영채', '박유진', '이세연']

idx = random.randint(0, len(students)-1)
print(f'{students[idx]}님, 너 나와!')

#리스트의 원소 중 1개를 무작위로 선택 -> 반환
student = random.choice(students)
print(f'{student}님, 너 나와!')

# 리스트 원소 중에서, n개를 무작위 선택
random.sample
#sample 단어 = 표본 -> 전체 중 몇개를 표본으로 뽑는다는 얘기/ population 모집단(전체집합) 중 몇개 뽑고 싶은지 입력
leaders  = random.sample(students,2)

# 랜덤한 사람 뽑기? 
print(f'7기 리더는? {leaders}')
#중복을 선택하지 않고 갯수 중에서 몇개만 뽑아낼 수 있는게 sample 함수라는거 기억하기 
