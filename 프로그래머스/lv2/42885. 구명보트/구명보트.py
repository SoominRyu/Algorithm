def solution(people, limit):
    people.sort(reverse = True)
    
    answer = 0
    
    left = 0 # 무거운 사람 탐색
    right = len(people) -1 # 가벼운 사람 탐색
    
    while left < right :
        # print(people[left], people[right])
        if people[left] + people[right] <= limit :
            right -= 1
            answer += 1
        left += 1

    return len(people) - answer



# 테스트케이스 통과 / 효율성 실패 

# def solution(people, limit):
#     people.sort(reverse = True)
#     b = [[limit,0]]
#     # answer = 1
#     for i in range(len(people)):
#         print(people)
#         last = 0
#         for j in range(len(b)):
#             print(b)
#             if b[j][0] >= people[i] and b[j][1] < 2:
#                 b[j][0] -= people[i]
#                 b[j][1] += 1
#                 last = 1
#                 break
                
#             # last = j
                           
#         if last == 0:
#              b.append([limit-people[i],1])
    
        
#     answer = len(b)
#     # answer = 0
#     return answer