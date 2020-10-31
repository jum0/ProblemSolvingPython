def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0,0,0]
    answer = []
    
    for idx, ans in enumerate(answers):
        if ans == pattern1[idx%len(pattern1)]:
            scores[0] += 1
        if ans == pattern2[idx%len(pattern2)]:
            scores[1] += 1
        if ans == pattern3[idx%len(pattern3)]:
            scores[2] += 1
    
    for idx, score in enumerate(scores):
        if score == max(scores):
            answer.append(idx+1)
    
    return answer
