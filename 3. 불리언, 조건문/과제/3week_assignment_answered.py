# 문제 1번
def question1():
    return "next"

# 문제 2번
def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return "윤년입니다."
    else:
        return "윤년이 아닙니다."

# 문제 3번
def alram(time):
    hour = time // 100
    minute = time % 100

    if minute >= 45:
        minute -= 45
    elif minute < 45:
        hour -= 1
        minute += 15

    if hour >= 12:
        return "오후 " + str(hour) + "시 " + str(minute) + "분"
    elif hour < 12:
        return "오전 " + str(hour) + "시 " + str(minute) + "분"

# 문제 4번
def findDaesun(x1,y1,r1,x2,y2,r2):
    def distance(x1,y1,x2,y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    park_choi = distance(x1,y1,x2,y2)

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            return "어딘지 모르겠다 오바"
        else:
            return 0
    else:
        if r1 + r2 < park_choi or abs(r1-r2) > park_choi:
            return 0

        elif r1 + r2 == park_choi or abs(r1-r2) == park_choi:
            return 1

        elif r1 + r2 > park_choi > abs(r1-r2):
            return 2
