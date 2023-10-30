import random

# 수정된 데이터를 리스트로 저장
data = {
    1: 100,
    2: 50,
    3: 33.333,
    4: 25,
    5: 20,
    6: 16.666,
    7: 14.285,
    8: 12.5,
    9: 11.111,
    11: 9.0909,
    12: 8.333,
    13: 7.692,
    14: 7.142,
    15: 6.666,
    16: 6.25,
    17: 5.882,
    18: 5.555,
    19: 5.263
}

exclude_numbers = [10, 1,2,3,8,4,5,18,19,9]


while True:
    # 1에서 19까지의 무작위 숫자 생성
    random_number =  random.choice([num for num in range(1, 20) if num not in exclude_numbers])
    if random_number == 10:
        continue
    
    # 해당 숫자에 대한 데이터 출력
    correct_answer = data[random_number]
    print(f"표에서 숫자 {random_number}에 대한 결과는 무엇인가요?")
    user_answer = input("답을 입력하세요: ")
    
    if user_answer == '':
        print(f"정답은 {correct_answer}입니다.")
        print("\n\n")
        continue
    # 사용자 입력과 정답 비교
    if float(user_answer) == correct_answer:
        print("정답입니다!")
        #세줄 건너띄기
        print("\n\n")
    else:
        print(f"틀렸습니다. 정답은 {correct_answer}입니다.")
        #세줄 건너띄기
        print("\n\n")

    