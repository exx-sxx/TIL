
import time
import random

# 오늘의 발표자 뽑기 
# 분단 별로 발표자를 뽑으려고 합니다.

# 1분단 
students1 = '김화영','김지민','유수진','윤수정','이은선','곽지민','류용윤'

# 2분단 
students2 = '김민정','조은별','최은지','유영채','정진용','박유진','김태현','이세연' 
# 1. 데이터를 어떻게 구조화 하면 좋을까요?
# 2. 구조화한 데이터를 가지고, 분단별 발표자를 뽑아 보세요.

student1 = random.choice(students1)
student2 = random.choice(students2)
print(f'1분단 발표자는 {student1}, 2분단 발표자는 {student2} 입니다')
