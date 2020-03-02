
"""遗传算法实现求函数极大值—Zjh"""
import numpy as np
import random
import matplotlib.pyplot as plt
class Ga():
    """求出二进制编码的长度"""
    def __init__(self):
        self.boundsbegin = -2
        self.boundsend = 3
        precision = 0.0001 # 运算精确度
        self.Bitlength = int(np.log2((self.boundsend - self.boundsbegin)/precision))+1#%染色体长度
        self.popsize = 50# 初始种群大小
        self.Generationmax = 12# 最大进化代数
        self.pcrossover = 0.90# 交叉概率
        self.pmutation = 0.2# 变异概率
        self.population=np.random.randint(0,2,size=(self.popsize,self.Bitlength))
 
    """计算出适应度"""
    def fitness(self,population):
        Fitvalue=[]
        cumsump = []
        for i in population:
            x=self.transform2to10(i)#二进制对应的十进制
            xx=self.boundsbegin + x * (self.boundsend - self.boundsbegin) / (pow(2,self.Bitlength)-1)
            s=self.targetfun(xx)
            Fitvalue.append(s)
        fsum=sum(Fitvalue)
        everypopulation=[x/fsum for x in Fitvalue]
        cumsump.append(everypopulation[0])
        everypopulation.remove(everypopulation[0])
        for j in everypopulation:
            p=cumsump[-1]+j
            cumsump.append(p)
        return Fitvalue,cumsump
    """选择两个基因，准备交叉"""
    def select(self,cumsump):
        seln=[]
        for i in range(2):
            j = 1
            r=np.random.uniform(0,1)
            prand =[x-r for x in cumsump]
            while prand[j] < 0:
                j = j + 1
            seln.append(j)
        return seln
    """交叉"""
    def crossover(self, seln, pc):
        d=self.population[seln[1]].copy()
        f=self.population[seln[0]].copy()
        r=np.random.uniform()
        if r<pc:
            print('yes')
            c=np.random.randint(1,self.Bitlength-1)
            print(c)
            a=self.population[seln[1]][c:]
            b=self.population[seln[0]][c:]
            d[c:]=b
            f[c:]=a
            print(d)
            print(f)
            g=d
            h=f
        else:
            g=self.population[seln[1]]
            h=self.population[seln[0]]
        return g,h
    """变异操作"""
    def mutation(self,scnew,pmutation):
        r=np.random.uniform(0, 1)
        if r < pmutation:
            v=np.random.randint(0,self.Bitlength)
            scnew[v]=abs(scnew[v]-1)
        else:
            scnew=scnew
        return scnew
 
    """二进制转换为十进制"""
    def transform2to10(self,population):
        #x=population[-1]  #最后一位的值
        x=0
        #n=len(population)
        n=self.Bitlength
        p=population.copy()
        p=p.tolist()
        p.reverse()
        for j in range(n):
            x=x+p[j]*pow(2,j)
        return x  #返回十进制的数
    """目标函数"""
    def targetfun(self,x):
        #y = x∗(np.sin(10∗(np.pi)∗x))+ 2
        y=x*(np.sin(10*np.pi*x))+2
        return y
 
if __name__ == '__main__':
    Generationmax=12
    gg=Ga()
    scnew=[]
    ymax=[]
    #print(gg.population)
    Fitvalue, cumsump=gg.fitness(gg.population)
    Generation = 1
    while Generation < Generationmax +1:
        Fitvalue, cumsump = gg.fitness(gg.population)
        for j in range(0,gg.popsize,2):
            seln = gg.select( cumsump)  #返回选中的2个个体的序号
            scro = gg.crossover(seln, gg.pcrossover)  #返回两条染色体
            s1=gg.mutation(scro[0],gg.pmutation)
            s2=gg.mutation(scro[1],gg.pmutation)
            scnew.append(s1)
            scnew.append(s2)
        gg.population = scnew
        Fitvalue, cumsump = gg.fitness(gg.population)
        fmax=max(Fitvalue)
        d=Fitvalue.index(fmax)
        ymax.append(fmax)
        x = gg.transform2to10(gg.population[d])
        xx = gg.boundsbegin + x * (gg.boundsend - gg.boundsbegin) / (pow(2, gg.Bitlength) - 1)
        Generation = Generation + 1
    Bestpopulation = xx
    Targetmax = gg.targetfun(xx)
    print(xx)
    print(Targetmax)
 
x=np.linspace(-2,3,30)
y=x*(np.sin(10*np.pi*x))+2
plt.scatter(2.65,4.65,c='red')
plt.xlim(0,5)
plt.ylim(0,6)
plt.plot(x,y)
plt.annotate('local max', xy=(2.7,4.8), xytext=(3.6, 5.2),arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
