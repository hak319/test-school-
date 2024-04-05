def account():
    print("새로운 계좌를 개설")

account()

def deposit(balance , money):
    print("{0}원을 입금합니다. 잔액은 {1}원 입니다".format(money, balance + money))
    return balance + money

def withdraw(balance, money):  # balance와 money 매개변수 추가
    if balance >= money:
        print("{0}원을 출금합니다. 잔액은 {1}원입니다".format(money, balance - money))
        return balance - money
    else:
        print("잔액이 부족합니다. 잔액은 {0}원입니다".format(balance))
        return balance

balance = 0 # 초기잔액
balance = deposit(balance, 1000) # 1000원 입금
balance = withdraw(balance, 2000) # 출금시도 -> 실패
balance = withdraw(balance, 500) # 출금 시도 -> 성공
