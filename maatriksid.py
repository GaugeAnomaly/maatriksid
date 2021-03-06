#encoding: utf-8
"""
Lühike kasutusjuhend:
maatriksid.py on Pythoni teek, mis võimaldab teha lihtsaid arvutusi maatriksitega.
Kõik maatriksitega seotud funktsioonid ja operatsioonid mida saab selle teegiga kasutada
on välja toodud Maatriksi klassi kirjelduses. Lisaks sellele on teegis kaks funktsiooni: skalaar(v1,v2),
mis annab vektorite skalaarkorrutise; fillMatrix(n,m,fun), mis loob uue maatriksi mõõtmetega n x m
ja arvutab igale elemendile väärtuse funktsiooniga fun (fun on fillMatrixi argument, mis on funktsiooni tüüpi).
Igal maatriksil on oma meetod .printMatrix(), mis ei võta argumente (prindib välja maatriksi, mis seda meetodi
kutsub). Kui tekib küsimusi või leidub vigu, saatke tagasisidet aadressile van_gentjanaare@hotmail.com
"""
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
    def rank(self):
        n = min([len(self.M),len(self.M[0])])
        dr = len(self.M)-len(self.M[0])
        if n == 1 and dr == 0 and self.det() == 0:
            return 0
        if fillMatrix(n,n,lambda x,y: self.M[x][y]).det() != 0:
            return n
        for i in range(abs(dr)):
            if dr > 0:
                if fillMatrix(n,n,lambda x,y: self.M[x+i+1][y]).det() != 0:
                    return n
            else:
                if fillMatrix(n,n,lambda x,y: self.M[x][y+i+1]).det() != 0:
                    return n
        astakud = []
        for i in range(len(self.M)):
            for j in range(len(self.M[0])):
                astakud.append(self.alamMaatriks(i,j).rank())
        return max(astakud)

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

    def alamMaatriks(self,i,j):
        return self.transpoos().drop(j).transpoos().drop(i)

    def miinor(self,i,j):
        return self.alamMaatriks(i,j).det()

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
            return print("Ei ole ruutmaatriks!")
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
        
    def __truediv__(self,x):
        print("division")
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
