import time
import random

# # 불 속성 마법을 배워야 하는 마법사가 되..

# print('time 모듈 어떻게 작동하는지 확인할게요.')

# for i in range(5): # i가 0부터 4까지 하나씩 되는거임 
#     print(5-i) # 5-i하면 5, 4, 3, 2, 1 이런 식으로 되는 거임 
#     time.sleep(1)

# print('어떻게 작동되는지 확인하셨죠?')
# # 프로그램 내의 고양감을 줌 웅웅 있어빌리티 


# 3. 카운트다운이 있는 로또 번호 추첨기 만들기
print('카운트다운이 있는 로또 번호 추첨기 만들기')

for i in range(5, 0, -1):  
    print(f'{i}초 남았습니다') # 5-i하면 5, 4, 3, 2, 1 이런 식으로 되는 거임 
    time.sleep(1)
    
numbers  = list(range(1,46))  #눈으로 보기 힘드니까 list로 변환 
lotto_number = random.sample(numbers,6)

lotto_num = lotto_number[:-1]
lotto_bonus = lotto_number[-1] # 달랑이라 못더함
lotto_number.sort() #리스트에 딸려 있는 메쏘드 = 오름차순 (작은 거 -> 큰 거)

print(f'로또 번호 {lotto_num}')
print(f'보너스 번호 {lotto_bonus}')

