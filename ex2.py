#[C_MM058-中] 二項式求解
while True:
    try:
        
        a = input().split(',')
        # x_coe * x + y_coe * y = c
        x_coe = int(a[0])
        y_coe = int(a[1])
        c     = int(a[2])

        for i in range(c+1):
            if (c-i) % y_coe == 0 and i%x_coe==0:
                x = i/x_coe
                y = (c-i)/y_coe
                print('%d,%d' %(x, y))
                
    except:
        break
