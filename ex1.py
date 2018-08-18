#[C_AR66-易] 撲克牌13點
a = input().split(' ')

# initialize summation
sum_card = 0

for i in a :
    #print(type(i))
    
    if i == 'A':
        sum_card += 14
    elif i == 'J':
        sum_card += 11
    elif i == 'Q':
        sum_card += 12
    elif i == 'K':
        sum_card += 13
    else:
        i=int(i)
        sum_card += i


print(sum_card)
