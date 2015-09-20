#encoding: utf-8
#Robin on siin
from copy import deepcopy

def skalaar(v1,v2):
    return sum([v1[x]*v2[x] for x in range(len(v1))])

def fillMatrix(n,m,fun):
    temp = []
    for i in range(n):
        temp.append([])
        for j in range(m):
            temp[i].append(fun(i,j))
    return Maatriks(temp)

class Maatriks:
    def rvec(self, n):
        return self.M[n]

    def vvec(self, n):
        return self.transpoos().M[n]

    def __init__(self,mlist):
        self.M = mlist

    def read_arv(self):
        return len(self.M)
    
    def veer_arv(self):
        return len(self.M[0])

    def transpoos(self):
        return Maatriks([list(x) for x in zip(*self.M)])

    def alamdet(self,i,j):
        return (-1)**(i+j) * self.miinor(i,j)

    def adj(self):
        return fillMatrix(self.read_arv(),self.veer_arv(),self.alamdet)

    def miinor(self,i,j):
        return self.transpoos().drop(j).transpoos().drop(i).det()

    def drop(self, i):
        temp = deepcopy(self.M)
        temp.pop(i)
        return Maatriks(temp)

    def pöörd(self):
        d = self.det()
        if d == 0:
            return print("Sellel maatriksil ei saa olla pöördväärtust!!!!")
        return self.transpoos().adj()*(1/d)

    def printMatrix(self):
        for i in self.M:
            for j in i:
                print(round(j,3),end='\t')
            print('\n')

    def det(self):
        n = self.read_arv()
        if n != self.veer_arv():
            return print("Ei ole ruutmaatriks!!!")
        if n == 0:
            return print("Maatriks on tyhi!!!!")
        if n == 1:
            return self.M[0][0]
        return sum([self.M[0][i]*self.alamdet(0,i) for i in range(n)])

    def __mul__(self, m2):
        if type(m2) is Maatriks:
            if self.veer_arv() != m2.read_arv():
                return print("Neid maatrikseid ei saa korrutada!!!!")
            return fillMatrix(self.read_arv(),m2.veer_arv(),lambda x,y: int(round(skalaar(self.rvec(x),m2.vvec(y)),3)))
        if type(m2) is int or type(m2) is float:
            return fillMatrix(self.read_arv(),self.veer_arv(),lambda x,y: self.M[x][y]*m2)
    
    def __rmul__(self, m2):
        if type(m2) is Maatriks:
            if self.read_arv() != m2.veer_arv():
                return print("Neid maatrikseid ei saa korrutada!!!!")
            return fillMatrix(m2.read_arv(),self.veer_arv(),lambda x,y: int(round(skalaar(m2.rvec(x),self.vvec(y)),3)))
        if type(m2) is int or type(m2) is float:
            return fillMatrix(self.read_arv(),self.veer_arv(),lambda x,y: self.M[x][y]*m2)
        
    def __div__(self,x):
        if type(x) is Maatriks:
            return print("Maatrikseid ei saa jagada!!!!!")
        if type(x) is int or type(x) is float:
            return fillMatrix(self.read_arv(),self.veer_arv(),lambda k,l: self.M[k][l]/x)

    def __add__(self,m2):
        if type(m2) is int or type(m2) is float:
            return print("Sa ei saa maatrikseid ja numbreid liita")
        if self.read_arv() != m2.read_arv() or self.veer_arv() != m2.veer_arv():
            return print("Neid maatrikseid ei saa liita!!!!")
        return fillMatrix(self.read_arv(),self.veer_arv(),lambda x,y: self.M[x][y]+m2.M[x][y])
