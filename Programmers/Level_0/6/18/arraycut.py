# 문제 설명
# 길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다. parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다. 각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# 1 ≤ my_strings의 길이 = parts의 길이 ≤ 100
# 1 ≤ my_strings의 원소의 길이 ≤ 100
# parts[i]를 [s, e]라 할 때, 다음을 만족합니다.
# 0 ≤ s ≤ e < my_strings[i]의 길이
# 입출력 예
# my_strings	parts	result
# ["progressive", "hamburger", "hammer", "ahocorasick"]	[[0, 4], [1, 2], [3, 5], [7, 7]]	"programmers"
# 입출력 예 설명
# 입출력 예 #1

# 예제 1번의 입력을 보기 좋게 표로 나타내면 다음과 같습니다.
# i	my_strings[i]	parts[i]	부분 문자열
# 0	"progressive"	[0, 4]	"progr"
# 1	"hamburger"	[1, 2]	"am"
# 2	"hammer"	[3, 5]	"mer"
# 3	"ahocorasick"	[7, 7]	"s"
# 각 부분 문자열을 순서대로 이어 붙인 문자열은 "programmers"입니다. 따라서 "programmers"를 return 합니다.

# 답:
def solution(my_strings, parts):
    answer = ''
    for i in range(0, len(my_strings)):
        j, k = parts[i]
        answer += my_strings[i][j:k+1]
    return answer

# 구간으로 칼질하기: 슬라이싱 (Slicing)

# 대괄호 안에 콜론(:)을 넣어 범위를 지정합니다. 가장 중요한 대원칙은 "시작은 포함하되 끝은 포함하지 않는다"는 점입니다.

# 기본 꼴: arr[시작위치 : 끝위치 : 증감폭]

# arr[s:e] (기본형): s번 방부터 e-1번 방까지 잘라냅니다. (글자 수가 정확히 e - s개가 됨)

# 앞서 풀었던 문제들처럼 길이가 l인 구간을 자르고 싶다면 끝자리에 반드시 시작점과 길이를 더한 s + l을 적어주어야 합니다. ➔ arr[s : s + l]

# arr[:e] / arr[s:] (생략형):

# 시작을 생략하면 무조건 0번 방부터 자릅니다. (arr[:3] ➔ 0, 1, 2번 방)

# 끝을 생략하면 리스트의 끝방까지 싹 다 가져옵니다. (arr[3:] ➔ 3번 방부터 끝까지)

# arr[::-1] (역순 치트키): 세 번째 자리에 -1을 주면 데이터를 뒤에서부터 거꾸로 뒤집은 새 배열을 만듭니다. (문자열 뒤집기 쿼리 문제의 치트키)