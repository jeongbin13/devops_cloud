def gugudan(number):
# number = 3
print(f"--- {number}단 ---")
for i in range(1, 10):
    print(f"{number} * {i} ={number * i}")

for j in range(1, 10):
    gugudan(j)

gugudan(3)
gugudan(4)
gugudan(5)
gugudan(6)
gugudan(7)

아래코드의 함수 호출부를 for반복문으로 변경



