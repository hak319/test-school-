def find_minji_position(passengers, stolen_seat):
    # stolen_seat보다 앞에 있던 사람들은 칸이 하나씩 밀림
    for i in range(len(passengers)):
        if passengers[i] >= stolen_seat:
            passengers[i] += 1
    # 민지가 몇 번째 칸에 탔는지 찾음
    for i in range(len(passengers)):
        if passengers[i] == "민지":
            return i + 1

# 초기 상태
passengers = ["철수", "짱구", "민지", "병준"]
stolen_seat = "병준"
# 칸을 뺏긴 상황
stolen_seat_index = passengers.index(stolen_seat)
passengers.pop(stolen_seat_index)
# 민지의 탑승 위치
minji_position = find_minji_position(passengers, stolen_seat_index)
# 결과 출력
print("민지는", minji_position, "번째 칸에 탔습니다.")