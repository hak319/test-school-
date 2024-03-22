temp = float(input("오늘온도는? : "))

if temp >= 30:
    print("너무 더워요")
elif temp >= 10:
    print("활동하기 좋은 날씨")
elif temp >= 0:
    print("외투를 챙기세요")
else:
    print("너무 추워요")
