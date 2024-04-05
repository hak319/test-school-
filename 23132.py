def account():
    print("새로운 계좌를 개설")

account()

def deposit(balance, money):
    print("{0}원을 입금합니다. 잔액은 {1}원 입니다".format(money, balance + money))
    return balance + money

def withdraw(balance, money): 
    commission = 100
    print("업무시간이외엔 {0}을 출금했습니다".format(money))
    return commission, balance - money - commission

balance = 0 
balance = deposit(balance, 1000)

commission, balance = withdraw(balance, 500)

print("수수료는 {0}원이며, 잔액은 {1}원입니다".format(commission, balance))