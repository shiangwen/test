import pandas as pd
'''
fruit=['banana','apple','kiwi','watermelon']
price=['10','20','8','80']

table = pd.Series(price,index=fruit)

print('banana的價格是',table['banana'])
print('kiwi的價格',table[2])
'''

'''
item=['book','ball','car','hat']
price=pd.Series([100,200,40,10])
counts=pd.Series([2,1,5,6])

total=price*counts
#很重要
total.index=item
print(total)
'''

name=['amy','john','max','hill']
english=[100,40,30,70]
math=[67,87,69,70]

dic={'English':english,'Math':math}
test_score=pd.DataFrame(dic,index=name)

# print(test_score)
# print(test_score.loc['max','Math'])

#排序小到大
englishsort=test_score.sort_values(by='English',ascending='False')
print(englishsort)
#排序大到小
englishsort2=test_score.sort_values(by='English',ascending='False')
print(englishsort2)