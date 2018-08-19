import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#設定圖表
fig = plt.figure(figsize=(10,5))
ax = plt.axes(xlim=(-6, 6),ylim=(0,40))
x, y = [], []
line, = plt.plot([], [],'ro',markersize=5)


#初始化函式:還原圖表內容
def init():
    line.set_data([], [])
    return line,

#更新函式:更新每一幀圖表當中的資料
def update(frame):
    start=-5
    
    x=[]
    for i in range(start,start+1+frame):
        x.append(i)
    y=[]    
    for j in x:
        y.append(2**(-j)+2)
    
    line.set_data(x, y)#設定要畫出來的資料
    return line,

ani = FuncAnimation(fig, update, frames=11,
                    init_func=init,interval=200)#每次畫圖時會將frames傳到更新函式中

#Set anime format
ax.set_aspect(1./ax.get_data_ratio())
plt.title('y=f(x)=2^(-x)+2')
plt.ylabel('y',rotation=0)
plt.xlabel('x')
plt.grid()
plt.show()