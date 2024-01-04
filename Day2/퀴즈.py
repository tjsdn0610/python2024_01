#1) 태어난 년도를 입력받고 현재 만나이 출력하는 프로그램
#ex) 2000-> 23

#2)세 개의 숫자를 입력 받고 총합, 평균(실수) 출력

# year=int(input("태어난 년도"))
# print(f"만나이 = {2024-year-1}")
#
#
# a = float(input("첫 번째:"))
# b= float(input("두번째:"))
# c= float(input("첫 번째:"))
# sum = a+b+c
# avg = sum/3
# print(f"총합: {sum}, 평균:{avg}")





#3_섭씨온도 입력받아 화씨 온도로 변환을 출력하는 프로그램 만들기
#F=C*5.9+32
#변수[실수]:.2f 둘째자리 출력

C= float(input("섭씨온도"))
print(f"F={C*5.9+32}")








#4)사용자의 키(m)와 몸무게(kg)를 입력받아 BMI출력하는 프로그램 만들기
#BMI = Weight/(heignt**2)
H = float(input("키"))
W = float(input("몸무게"))
print(f"BMI = {W/(H**2)}")




#5) 반지름 입력시 원의 넓이와 둘레를 구하는 프로그램
r = float(input("반지름"))
W = 3.14*r**2
R = 2*3.14*r
print(f"원의 넓이 = {W}, 원의 둘레 = {R}")



#print()-출력
#input()-입력[결과:문자 타입]
# 변수 - 임시 저장하는 곳
#int()/float()/str()
#사칙연산- +,-,*,/(나누기),%(나머지),//(몫),**(제곱)
