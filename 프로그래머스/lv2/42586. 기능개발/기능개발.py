import math

def solution(progresses, speeds):
    answer = []
    percent = [100-i for i in progresses]
    
    days = list()
    
    for j in range(len(progresses)):
        days.append(math.ceil(percent[j]/speeds[j]))
    
    day = 0
    count = 0
    
    for d in range(len(days)):
        if day < days[d]:
            answer.append(count)
            day = days[d]
            count = 1
            # print("if", answer, count, day, days[d])
        else:
            count +=1
            # print("else", answer, count, day, days[d])
        
        if d == len(days) - 1:
            answer.append(count)
            return answer[1:]
        
        