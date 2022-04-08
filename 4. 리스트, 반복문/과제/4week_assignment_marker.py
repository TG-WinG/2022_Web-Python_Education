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

    if lowPoint >= 0:
        answer = "아니야 조금만 더 기다려" 
    
    else:
        answer = "%s일 전에 샀어야지 으이구" %lowDay

    return answer

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




# -------------------------------------------------------------------------------- #
def intervention_solved(queue):
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
def pascal_solved(n):
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
def auto_complete_solved(entry, searchWords):
    answer = list()
    
    for i in searchWords:
        if entry in i:
            answer.append(i)
    
    answer.sort()

    return answer

# 문제 4번
def stock_price_solved(change):
    
    # 시세 변동(change)를 가격(price)으로 변경
    for i in range(1, len(change)):
        change[i] = change[i-1]+change[i]
        
    # sum이랑 완전탐색으로 구할 수도 있으나, 최저가때 구입하는 것이 제일 이득
    today_price = change[-1]
    lowest_price = min(change)
    
    if today_price - lowest_price<=0 : 
        return "아니야 조금만 더 기다려"
    else:
        change.reverse()
        return str(change.index(lowest_price)) + "일 전에 샀어야지 으이구"


# 문제 5번
def decryption_solved(letter):
    answer = str()
    
    before = "defghijklmnopqrstuvwxyzabc"
    after = "abcdefghijklmnopqrstuvwxyz"

    for i in letter:
        if i in before:
            answer += after[before.index(i)]
        else:
            answer += i

    return answer

OXList = list()
point = 0

def q1():
    if not intervention(["아린", "성은", "지호", "유아", "미미", "우기"]) == intervention_solved(["아린", "성은", "지호", "유아", "미미", "우기"]):
        OXList.append('X')
        return 0
    if not intervention(["아린", "슈화", "지호", "유아", "성은", "우기"]) == intervention_solved(["아린", "슈화", "지호", "유아", "성은", "우기"]):
        OXList.append('X')
        return 0
    if not intervention(["아린", "슈화", "지호", "성은", "미미", "우기"]) == intervention_solved(["아린", "슈화", "지호", "성은", "미미", "우기"]):
        OXList.append('X')
        return 0
    if not intervention(["아린", "우기", "지호", "유아", "미미", "성은"]) == intervention_solved(["아린", "우기", "지호", "유아", "미미", "성은"]):
        OXList.append('X')
        return 0
    if not intervention(["아린", "슈화", "지호", "유아", "미미", "우기"]) == intervention_solved(["아린", "슈화", "지호", "유아", "미미", "우기"]):
        OXList.append('X')
        return 0
    if not intervention(["아린", "성은", "지호", "유아", "미미", "우기", "슈화"]) == intervention_solved(["아린", "성은", "지호", "유아", "미미", "우기", "슈화"]):
        OXList.append('X')
        return 0
    if not intervention(["아린", "성운", "지호", "유아", "미미", "우기", "성원"]) == intervention_solved(["아린", "성운", "지호", "유아", "미미", "우기", "성원"]):
        OXList.append('X')
        return 0
    OXList.append('O')
    return 10

def q2():
    if not pascal(3) == pascal_solved(3):
        OXList.append('X')
        return
    if not pascal(15) == pascal_solved(15):
        OXList.append('X')
        return
    if not pascal(21) == pascal_solved(21):
        OXList.append('X')
        return
    if not pascal(30) == pascal_solved(30):
        OXList.append('X')
        return
    if not pascal(24) == pascal_solved(24):
        OXList.append('X')
        return
    OXList.append('O')
    return 15

def q3():
    siteDB = ["메이플스토리", "넥슨", "티지윙", "아이돌", "아이즈원", "미친놈", "죽일놈", "강아지 분양", "미친 강아지", "데이터", "메이플 직업 추천", "아이들", "소녀시대", "오마이걸 신곡", "프로야구", "대학교", "대학교 개강", "대학교 입시", "대학생 공모전", "컴퓨터 공학과", "컴퓨터 가게", "경기도 남양주시", "경기도 용인시", "경기도 수원시", "서울특별시 노원구", "서울특별시 송파구"]
    if not auto_complete("강아지", siteDB) == auto_complete_solved("강아지", siteDB):
        OXList.append('X')
        return
    if not auto_complete("메이플", siteDB) == auto_complete_solved("메이플", siteDB):
        OXList.append('X')
        return
    if not auto_complete("아이돌", siteDB) == auto_complete_solved("아이돌", siteDB):
        OXList.append('X')
        return
    if not auto_complete("경기도", siteDB) == auto_complete_solved("경기도", siteDB):
        OXList.append('X')
        return
    if not auto_complete("서울", siteDB) == auto_complete_solved("서울", siteDB):
        OXList.append('X')
        return
    if not auto_complete("아이", siteDB) == auto_complete_solved("아이", siteDB):
        OXList.append('X')
        return
    if not auto_complete("야구", siteDB) == auto_complete_solved("야구", siteDB):
        OXList.append('X')
        return
    OXList.append('O')
    return 15

def q4():
    if not stock_price([0,1,2,3,4,5,6,7,8,9,0]) == stock_price_solved([0,1,2,3,4,5,6,7,8,9,0]):
        OXList.append('X')
        return 0
    if not stock_price([0,3,4,-1,-3,-4,-6,1,3,5,-3]) == stock_price_solved([0,3,4,-1,-3,-4,-6,1,3,5,-3]):
        OXList.append('X')
        return 0
    if not stock_price([0,1,2,-14,3,4,-6,4,2,4,1]) == stock_price_solved([0,1,2,-14,3,4,-6,4,2,4,1]):
        OXList.append('X')
        return 0
    if not stock_price([-2,-3,-5,6,4,10,-35,3,4,1,3]) == stock_price_solved([-2,-3,-5,6,4,10,-35,3,4,1,3]):
        OXList.append('X')
        return 0
    if not stock_price([0,1,2,-3,3,2,2,-3,1,-2,-3]) == stock_price_solved([0,1,2,-3,3,2,2,-3,1,-2,-3]):
        OXList.append('X')
        return 0
    if not stock_price([2600,-3333,-1353,2341,-3513,3465,5412,-3511,-3654,-3525,7332]) == stock_price_solved([2600,-3333,-1353,2341,-3513,3465,5412,-3511,-3654,-3525,7332]):
        OXList.append('X')
        return 0
    if not stock_price([-1, -2, 0, 0, 1, 2, 3, 4, -10, 2]) == stock_price_solved([-1, -2, 0, 0, 1, 2, 3, 4, -10, 2]):
        OXList.append('X')
        return 0
    if not stock_price([-1, -2, 3, -7, 2, 4, -5, 6, 0, 1]) == stock_price_solved([-1, -2, 3, -7, 2, 4, -5, 6, 0, 1]):
        OXList.append('X')
        return 0

    OXList.append('O')
    return 30

def q5():
    if not decryption("asdvxczbk asdf! fsdhknzvas!@#!$ asdfnkjasfbv") == decryption_solved("asdvxczbk asdf! fsdhknzvas!@#!$ asdfnkjasfbv"):
        OXList.append('X')
        return 0
    if not decryption("asbkjnasdljbn ajslkdn$%&%$^#*& asdfaksdnmfk") == decryption_solved("asbkjnasdljbn ajslkdn$%&%$^#*& asdfaksdnmfk"):
        OXList.append('X')
        return 0
    if not decryption("dsakvkcx.znvknuilehgasj,fdbna,.as/vcxzvika!@#!@sakvcnaskjlv") == decryption_solved("dsakvkcx.znvknuilehgasj,fdbna,.as/vcxzvika!@#!@sakvcnaskjlv"):
        OXList.append('X')
        return 0
    if not decryption("ask.vnujlqawherblukjbvnafsjdfngvas/df/as,vasilk;hvnlujasbvc@$%$!@#asdkjcvnv") == decryption_solved("ask.vnujlqawherblukjbvnafsjdfngvas/df/as,vasilk;hvnlujasbvc@$%$!@#asdkjcvnv"):
        OXList.append('X')
        return 0
    OXList.append('O')
    return 30

point = q1() + q2() + q3() + q4() + q5()

print("점수: %s" %point)
print("--------정오표--------")
for i in range(5):
    print("%s번 문항: %s" %(i+1,OXList[i]))