# 1000 미만의 자연수 중에서 3과 5의 공통배수의 개수 구하기

# 구조 생각해보기
# 1. 입력받기
# -> 1 이상 1000 미만의 자연수 입력받기
# 2. 개수 구하기
# -> three_five_mul() 함수를 통해 입력받은 수 중 3과 5의 공통 배수의 개수 구하기
# 3. 출력하기
# -> 구해놓은 개수룰 출력하기

A = 0
while True :
    a = int(input('1 이상 1000 미만의 자연수 중 임의의 숫자를 입력해주세요 : '))
    if a < 1 or a > 999 :
        print('다시 입력해주세요.')
    else :
        print('구하는 중입니다...')
        break

def three_five_mul(num) :
    count = 0
    if num == 1 :
        print('3과 5의 공통배수가 없습니다.')
    for i in range(1, num) :
        if i % 3 == 0 and i % 5 == 0 :
            count = count + 1
    return count

RESULT = three_five_mul(a)

print(f'입력하신 수 미만의 3과 5의 공통 배수는 {RESULT}개입니다.')
