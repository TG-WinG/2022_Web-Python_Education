#문제 1번
def sum(a,b):
    return a+b

#문제 2번
def sub(a,b):
    return a-b

#문제 3번
def mul(a,b):
    return a*b

#문제 4번
def div(a,b):
    return a/b

# 문제 5번
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

# 문제 6번
def short():
    lylic = "life is short art is long"
    return lylic[8:13]

# 문제 7번
def myReverse(string):
    return string.reverse()

# 문제 8번
def letMeIntroduceMyself():
    name = input("이름을 입력하시오: ")
    hobby = input("취미를 입력하시오: ")
    school = input("재학 중인 대학을 입력하시오: ")
    birth = input("생일을 입력하시오(예시: 981128): ")
    myselfStr = "제 이름은 " + name + "입니다. 제 취미는 " + hobby + "이구요, 저는 " + school + "를 다니고 있습니다. 제 생일은 " + birth[2:4] + "월 " + birth[4:6] + "일 입니다."
    print(myselfStr)
    return myselfStr

# 문제 9번
def calcAI():
    num1 = input("첫 번째 숫자를 입력하시오: ")
    num2 = input("두 번째 숫자를 입력하시오: ")
    sum = int(num1) + int(num2)
    msg = "두 수의 합은 " + str(sum) + "입니다."
    print(msg)
    return msg