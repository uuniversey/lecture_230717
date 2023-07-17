
#연습문제 

#2.1.1

# cases = int(input())

# num = 1
# while num <= cases:
#     print(cases)
#     num = num + 1



#2.1.2

# cases = int(input())

# num = 1
# while num <= cases:
#     print(num, num*num)
#     num = num + 1



# 2.1.3

# num = int(input())

# i = 1
# while i <= num:
#     height = 100 * 0.6 ** i
#     result = round(height, 4)
#     print(i, result)
#     i = i + 1



# 2.1.4

# number = 358
# rem = rev = 0
# while number >= 1:
#     rem = number % 10
#     rev = rev * 10 + rem
#     number = number // 10
# print(rev)



# 2.2.1 

# num = int(input())

# if num == 1:
#     print('일')
# elif num == 2:
#     print('이')
# else:
#     print('삼')



# 2.2.2

# print ('나이를 입력하세요:')
# how_old = int(input())
# if how_old <= 1924:
#     print('가장 위대한 세대')
# elif 1925 <= how_old <= 1945:
#     print('침묵 세대')
# elif 1946 <= how_old <= 1964:
#     print('베이비붐 세대')
# elif 1965 <= how_old <= 1980:
#     print('X 세대')
# elif 1981 <= how_old <= 1996:
#     print('밀레니얼 세대')        
# else:
#     print('Z 세대')


# 2.2.3

# num = int(input())
# text_M = str(num // 1000000)
# text_K = str(num // 1000)
# if num >= 1000000:
#     print (text_M + 'M')
# elif 1000000 > num >= 1000:
#     print (text_K + 'K')
# else:
#     print (num)


# 2.2.4

# sum = 0

# while True:
#     num = int(input())
#     if num < 0:
#         break
#     else:
#         sum += num

# print(sum)


# 2.2.5

# years = int(input())

# if years % 4 == 0:
#     if years % 100 == 0:
#         if years % 400 == 0:
#             print('윤년입니다.')
#         else:
#             print('평년입니다.')
#     else:
#         print('윤년입니다.')
# else: 
#     print('평년입니다.')


# 2.3.1

family = ['mother', 'father', 'me', 'manjudang']

for x in family:
    print (x,len(x))