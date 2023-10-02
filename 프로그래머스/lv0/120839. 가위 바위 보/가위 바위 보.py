# def solution(rsp):
#     answer = ''
    
#     rsp = list(rsp)
    
#     for i in rsp:
#         if i == "2":
#             answer += "0"
#         elif i == "0":
#             answer += "5"
#         elif i == "5":
#             answer +="2"
    
#     return answer

# dict 이용
def solution(rsp):
    answer = {'0':'5','2':'0','5':'2'}
    return ''.join(answer[i] for i in rsp)