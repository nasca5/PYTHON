# 2. 자료형

# 1.
# score = {'국어' : 80, '영어' : 75, '수학' : 55}
# sum = 0;
# for i in score.values() :
#   sum += i

# print(sum/3)


# 2.
# a = 13

# if(a%2 == 1) :
#   print('odd')
# else :
#   print('even')

# 3, 4
# pin = '881120-1068234'

# yyyymmdd = '19' + pin[:6]
# num = pin[7:]
# print(yyyymmdd)
# print(num)

# sex = pin[7]

# print(sex)

# 5.
# a = 'a:b:c:d'

# print(a.replace(':','#'))

# 6.
# a = [1, 3, 5, 4, 2]

# a.sort()
# a.reverse()

# print(a)

# 7.
# a = ['Life', 'is', 'too', 'short']

# result = ' '.join(a)
# print(result)

############################################################################################################################################################

# 3. 제어문

# 2.
# result = 0
# i = 1
# while i <= 1000 :
#   if (i % 3) == 0 :
#     result += i
#   i += 1
# print(result)

# 3.
# i = 0
# for i in range(1, 6) :
#   for j in range(1, i+1) :
#     print('*', end = "")
#   print(' ')

# 5. 
# A = [70, 60, 55, 75, 90, 80, 80, 85, 100]
# total = 0
# cnt = 0
# for score in A :
#   total += score
#   cnt += 1

# total = total / cnt

# print(total) 

#6. 
# numbers = [1, 2, 3, 4, 5]

# result = [num * 2 for num in numbers if num % 2 == 1]
# print(result)

############################################################################################################################################################

# 4. 사용자 입력과 출력 

# 1. 
# def is_odd(Number) :
#   if Number % 2 ==  1 :
#     print('%d는 홀수입니다.' % Number)
#   else :
#     print('%d는 짝수입니다.' % Number)
    
# a = int(input('판별하고 싶은 수를 입력하세요 :'))

# is_odd(a)

# 2. 
# def avg_numbers(*args) :
#   result = 0
#   for i in args :
#     result += i
#   return result / len(args)

# print(avg_numbers(1, 2, 3, 4, 5, 6, 7))

# 3.
# input1 = int(input('첫 번째 숫자를 입력하세요 : '))
# input2 = int(input('두 번째 숫자를 입력하세요 : '))

# total = input1 + input2

# print('두 수의 합은 %d입니다' % total)

# 5.
# with open("test.txt", "w") as f1 :
#   f1.write("Life is too short")

# with open("test.txt", "r") as f2 :
#   print(f2.read())

# 6. 
# user_input = input("저장할 내용을 입력하세요 : ")

# with open("test.txt", "a") as f1 :
#   f1.write(user_input + '\n')
  

# with open("test.txt", "r") as f2 :
#   print(f2.read())

# 7.
# with open("test.txt", "r") as f1 :
#   body  = f1.read()

# body = "Life is too short\nyou need Python"

# with open("test.txt", "w") as f2 :
#   f2.write(body)
  
# print(body)