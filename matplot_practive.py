import matplotlib.pyplot as plt
import pandas as pd

#plt.figure(facecolor='y')
plt.rcParams['font.sans-serif']=['Impact']# 重要！！！！！可以顯示中文
plt.plot([2,3,5],[5,4,7],color='wheat',linestyle='--')
plt.xlabel('days')
plt.ylabel('numbers')
plt.title('hello')
plt.show()
#plt.plot()
'''
price=pd.Series([15,20,6,9])
count=pd.Series([1,3,2,8])
total_price=price*count
fruit_index=['apple','banana','orange','watermelon']

plt.bar(fruit_index,total_price,color='g')
plt.show()
'''