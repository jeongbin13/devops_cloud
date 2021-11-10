import random

count = 0
number = random.randint(1, 101)
print("1 부터 100까지의 숫자를 10번 안에 맞춰보세요.")

while count < 10:
    count += 1
    user_input = int(input("몇 일까요"))
    if user_input == number:
        break

if user_input == number:
    print("ㅇㅇ."format(number))

else:
    print("ㅋㅋ."format(number))    
