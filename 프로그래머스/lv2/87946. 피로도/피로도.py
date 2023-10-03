from itertools import permutations as p

def solution(k, dungeons):
    answer = 0
    now_k = k
    l = len(dungeons)
    
    for dungeon in p(dungeons,l):
        result = 0
        k = now_k
        for i in dungeon:
            if k>=i[0]:
                result += 1
                k -= i[1]
        answer = max(answer, result)

        if answer == l:
            break
                    
    return answer



# 테케 9, 13 실패
# def solution(k, dungeons):
    
#     dungeons.sort(key = lambda x:x[0], reverse=True) 
#     dungeons.sort(key = lambda x:x[1]) 
#     dungeons.sort(key = lambda x:x[0]-x[1], reverse=True) 
#     # print(dungeons)
#     answer = 0

#     for i in dungeons:
#         if k>=i[0] and k-i[1]>=0:
#             answer += 1
#             k -= i[1]
        
#     return answer