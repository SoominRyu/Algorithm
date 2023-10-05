import math

def solution(progresses, speeds):
    answer = []
    percent = [100-i for i in progresses] # 남은 작업%
    
    days = list() # 작업 기간
    for j in range(len(progresses)):
        days.append(math.ceil(percent[j]/speeds[j]))
    
    day, count = 0, 0
    
    for d in range(len(days)):
        if day < days[d]:
            answer.append(count)
            day = days[d]
            count = 1
        else:
            count +=1
        
        if d == len(days) - 1:
            answer.append(count)
            return answer[1:]