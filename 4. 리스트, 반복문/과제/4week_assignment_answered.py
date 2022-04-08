# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 입력을 요구하는 문제가 없습니다.
# answer 변수를 사용하여 문제를 풀이하세요. 반환값은 answer 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 5일 23시 59분.
# 지각 제출 기한: 2022년 4월 6일 23시 59분. 주차 점수에서 20% 감점

# 문제 1번

def intervention(queue):
    answer = list()
    answer = queue

    sungeunIndex = 0
    if "성은" in answer:
        sungeunIndex = answer.index("성은")

    if sungeunIndex < 4:
        answer.append("승호")

    else:
        answer.insert(sungeunIndex+1, "승호")

    return answer

# 문제 2번
def pascal(n):
    answer = list()

    if n == 1:
        answer = [1]
    
    elif n == 2:
        answer = [1, 1] 

    else:
        answer = [1, 1]

    for i in range(n-2):
        nextPascal = [1]
        for j in range(i+1):
            nextPascal.append(answer[j]+answer[j+1])
        nextPascal.append(1)
        answer = nextPascal
    return answer 

# 문제 3번
def auto_complete(entry, searchWords):
    answer = list()
    
    for i in searchWords:
        if entry in i:
            answer.append(i)
    
    answer.sort()

    return answer

print(auto_complete("강아지", ["커피", "강아지무료분양", "강아지그림", "비숑", "비숑강아지"]))

# 문제 4번
def stock_price(stockChart):
    answer = str()
    lowPoint = 0
    lowDay = 0
    price = 0
    day = len(stockChart) - 1

    for i in stockChart:
        price += i
        if lowPoint >= price:
            lowPoint = price
            lowDay = day
        day -= 1

    if lowPoint == price or lowPoint >= 0:
        answer = "아니야 조금만 더 기다려"
    
    else:
        answer = "%s일 전에 샀어야지 으이구" %lowDay

    return answer

print(stock_price([-1, -2, 0, 0, 1, 2, 3, 4, -10, 2]))
print(stock_price([-1, -2, 3, -7, 2, 4, -5, 6, 0, 1]))

# 문제 5번
def decryption(letter):
    answer = str()
    
    before = "defghijklmnopqrstuvwxyzabc"
    after = "abcdefghijklmnopqrstuvwxyz"

    for i in letter:
        if i in before:
            answer += after[before.index(i)]
        else:
            answer += i

    return answer

def encryption(letter):
    answer = str()
    
    after = "defghijklmnopqrstuvwxyzabc"
    before = "abcdefghijklmnopqrstuvwxyz"

    for i in letter:
        if i in before:
            answer += after[before.index(i)]
        else:
            answer += i

    return answer

print(decryption("def"))
