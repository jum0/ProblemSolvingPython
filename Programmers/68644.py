# sol 1.
def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            if numbers[i]+ numbers[j] not in answer:
                answer.append(numbers[i]+ numbers[j])
    answer.sort()
    return answer


# sol 2.
def solution(numbers):
    answers = []
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            answers.append(numbers[i] + numbers[j])
            
    return sorted(set(answers))
