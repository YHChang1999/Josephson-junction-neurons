#引入畫圖標頭檔
import matplotlib.pyplot as plt     #畫圖用
import math     #三角函數用

#

#
#模擬輸入
start=0     #開始時間
finish=100  #停止時間
I_b=1.7
Lambda=0.1
Lambda_s=0.5
Lambda_p=0.5
Lambda_c=0
Gamma=1
eta=1
startval=[0,0,0,0]  #initial conditions
step=0.01  #每一個數值解的間距
#

#微分方程
def fy1(t,y1,y2,y3,y4):
    return y2
def fy2(t,y1,y2,y3,y4):
    return 0-Gamma*y2-math.sin(y1)-Lambda*(y1+y3)+Lambda_s*I_in*(t>30)*(t<35)+(1-Lambda_p)*I_b
def fy3(t,y1,y2,y3,y4):
    return y4
def fy4(t,y1,y2,y3,y4):
    return 0-Gamma*y4-math.sin(y3)+(-Lambda*(y1+y3)+Lambda_s*I_in*(t>30)*(t<35)-Lambda_p*I_b)/eta
#

#係數初始化
b=[1/6,1/3,1/3,1/6]
c=[[0,0,0,0],[0.5,0,0,0],[0,0.5,0,0],[0,0,1,0]]
d=[0,0.5,0.5,1]
k=[0,0,0,0]
order=4
#

#參數初始化
y1=startval[0]
y2=startval[1]
y3=startval[2]
y4=startval[3]
t=start
ck=0
#
#最後呈現的曲線陣列
Flux=[(y1+y3)*Lambda]
tvals=[start]
Input_strength=[]
Peak_Flux=[]

#

#Runge-Kutta Classical
#之前書上給的方法中使用最經典的方法
I_in=0.9
while I_in<=1.0:
    j=start+step
    while j<=finish:
        #對1
        k[0]=step*fy1(t,y1,y2,y3,y4)
        for i in range (1,order):
            ck=0
            for l in range(0,i):
                ck+=c[i][l]*k[l]
            k[i]=step*fy1(t+step*d[i],y1+ck,y2,y3,y4)
        y1tmp=y1
        for i in range (0,order):
            y1tmp+=b[i]*k[i]

        #對2
        k[0]=step*fy2(t,y1,y2,y3,y4)
        for i in range (1,order):
            ck=0
            for l in range(0,i):
                ck+=c[i][l]*k[l]
            k[i]=step*fy2(t+step*d[i],y1,y2+ck,y3,y4)
        y2tmp=y2
        for i in range (0,order):
            y2tmp+=b[i]*k[i]

        #對3
        k[0]=step*fy3(t,y1,y2,y3,y4)
        for i in range (1,order):
            ck=0
            for l in range(0,i):
                ck+=c[i][l]*k[l]
            k[i]=step*fy3(t+step*d[i],y1,y2,y3+ck,y4)
        y3tmp=y3
        for i in range (0,order):
            y3tmp+=b[i]*k[i]

        #對4
        k[0]=step*fy4(t,y1,y2,y3,y4)
        for i in range (1,order):
            ck=0
            for l in range(0,i):
                ck+=c[i][l]*k[l]
            k[i]=step*fy4(t+step*d[i],y1,y2,y3,y4+ck)
        y4tmp=y4
        for i in range (0,order):
            y4tmp+=b[i]*k[i]
        #上面都在做迭代
        t1=t+step
        #將迭代後的數值加入最後的陣列
        tvals.append(t1)
        t=t1
        y1=y1tmp
        y2=y2tmp
        y3=y3tmp
        y4=y4tmp
        j+=step
        Flux.append((y1+y3)*Lambda)
    Input_strength.append(I_in)
    Peak_Flux.append(max(Flux))
    I_in+=0.005
    y1=startval[0]
    y2=startval[1]
    y3=startval[2]
    y4=startval[3]
    t=start
    Flux=[(y1+y3)*Lambda]
    tvals=[start]
    ck=0
#

#畫圖

plt.plot(Input_strength,Peak_Flux)
plt.xlabel("Input strength (arb.units)")
plt.ylabel("Peak_Flux (arb.units)")
plt.title("FIG3-2")

plt.show()
#plt.savefig("FIG3-2.png",dpi=300,format="png")
#如果要存檔就把上一行的井字號去掉
#
