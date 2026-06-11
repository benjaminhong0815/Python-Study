# 문제 설명
# 정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 ≤ start_num ≤ end_num ≤ 50
# 입출력 예
# start_num	end_num	result
# 3	10	[3, 4, 5, 6, 7, 8, 9, 10]
# 입출력 예 설명
# 입출력 예 #1

# 3부터 10까지의 숫자들을 담은 리스트 [3, 4, 5, 6, 7, 8, 9, 10]를 return합니다.

# 답안:
def solution(start_num, end_num):
    answer = []
    for i in range(0, end_num- start_num + 1):
        answer.append(i + start_num)
    return answer

# 팁: 이 문제의 경우: list를 쓸 수 있음:
# def solution(start_num, end_num):
    # return list(range(start_num, end_num + 1))