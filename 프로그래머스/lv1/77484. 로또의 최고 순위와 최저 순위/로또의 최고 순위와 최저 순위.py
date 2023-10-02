def solution(lottos, win_nums):
    
    num0 = lottos.count(0)
    correct_num = len(list(set(lottos) & set(win_nums)))
    
    rank = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    answer = [rank[correct_num+num0], rank[correct_num]]
    
    return answer