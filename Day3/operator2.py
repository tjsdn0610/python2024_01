#산술 연산자 +,-,*,/,//,%,**    [결과:숫자]

#100이하의 정수를 입력받고 10의 자리와 1의 자리를 출력하는 프로그램
# num = int(input("100이하의 정수"))   #75
# ten = num //10   #7
# one = num%10     #5


#1000이하 정수를 입력받고 #분, 시로 환산하는 프로그램
#72 -> 1분 12초

num = int(input("1000이하의 정수"))
min = num//60
sec = num%60

print(f"시간={min}분 {sec}초")


#정수: 10000~99999사이 입력받고 100의자리 값 출력하는 프로그램
#ex) 17300->3
num = int(input("10000~99999사이 정수:"))
hun = num//100 #100이하 자리 없애기
result = hun % 10
print(result)












#비교 연산자[결과:Bool]
# >,<,<=,>=,==(같다),!=(다르다)

a= 3>1 #bool type
b= 3==1#bool type [Fales]
c= 3!=1#bool type [True]

# 논리연산자 [결과:bool]
# and : 피연산자가 모두 True이면 True
print(3>1 and 5>1) #True
#or: 피연산자가 하나라도 True이면 True
print(5<1 or 3<1 or 0<1) #True
#not: false->true, true->false
print(not(3>1)) # true->false


# 할당 연산자
a = 1
a = 3
#a얼마? 3 #3으로 갈아치우기
b=1
b=b+3 # 3 더해주기
b+=3 #3 더해주기
b-=3 #3 빼주기
b*=3 #3 곱하기
b/=3 #3나누기


