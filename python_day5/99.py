# 구구단 만들기

# 1 X 1 = 1 
# .....
# 1 X 9 = 9
# 2 x 1 = 2
# .....
# 9 X 0 = 81

# print()

# 이중 for 문, f-string 이용하여 만들어보자!

# 구구단을 외자 이중 for문
# 크게 1~9단 까지 , 한 단에서는 1~9가 순회

for i in range(1,10):
    print(f'{i}단입니다.')
    for j in range(1,10):
        print(f'{i} X {j} = {i*j}') #f string의 좋은점 : 간단한 계산도 가능 
