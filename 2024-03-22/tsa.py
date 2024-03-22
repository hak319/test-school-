li1 = ['철수', '짱구', '민지', '병준']
li1.insert(li1.index('병준') , '근영')
print(li1.index('민지'))
for i in range(len(li1)):
    li1.pop(0)
    print(li1)