def calculate_discount_and_gift(price):
    if price < 100:
        discount = price * 0.1
    else:
        discount = price * 0.15

        print("10층에서 사은품을 받아가세요.")
    
    total_price = price - discount
    
    if total_price < 100:
        gift = ""
    else:
        gift = "10층에서 사은품을 받아가세요."
    
    return total_price, gift

price = int(input("정가를 입력하시오 : "))
final_price, gift_message = calculate_discount_and_gift(price)

print("할인된 상품의 가격 = {}".format(final_price, gift_message))
