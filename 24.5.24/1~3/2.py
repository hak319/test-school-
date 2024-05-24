def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 3)

weight = float(input("몸무게를 KG 단위로 입력하시오: "))
height = float(input("키를 미터 단위로 입력하시오: "))

bmi = calculate_bmi(weight, height)
print("당신의 BMI = {:.3f}".format(bmi))