#encoding: utf-8
def skalaar(v1,v2):
    return sum([v1[x]*v2[x] for x in range(len(v1))])

class Maatriks:
    """M = [[1,2,3,4],
     [-3,-2,-3,-4],
     [8,-9,1,0],
     [0,-1,-2,2]]"""
     
    def vec(self, n):
        return self.M[n]

    def __init__(self,mlist):
        self.M = mlist

    def read_arv(self):
        return len(self.M)
    
    def veer_arv(self):
        return len(self.M[0])
    
    def printMatrix(self):
        for i in self.M:
            for j in i:
                print(j,end='\t')
            print('\n')

    def transpoos(self):
        return Maatriks([list(x) for x in zip(*self.M)])

    def miinor(self,i,j):
        temp = []
        c1 = 0
        for k in range(self.read_arv()):
            if k == i:
                continue
            temp.append([])
            for l in range(len(self.M[k])):
                if l == j:
                    continue
                temp[c1].append(self.M[k][l])
            c1 += 1
        return Maatriks(temp).det()

    def det(self):
        n = self.read_arv()
        if n != self.veer_arv():
            print("Ei ole ruutmaatriks!!!")
            return 0
        if n == 0:
            print("Maatris on tyhi!!!!")
            return 0
        if n == 1:
            return self.M[0][0]
        return sum([(-1)**i * self.M[0][i] * self.miinor(0,i) for i in range(n)])
        
    def pöörd(self):
        d = self.det()
        n = self.read_arv()
        if d == 0:
            print("Sellel maatriksil ei saa olla pöördväärtust!!!!")
            return
        M = []
        for i in range(n):
            M.append([])
            for j in range(n):
                M[i].append((-1)**(i+j)*self.transpoos().miinor(i,j)/d)
        return Maatriks(M)

    def __mul__(self, m2):
        if type(m2) is Maatriks:
            if self.read_arv() == [] or m2.read_arv() == 0:
                print("Maatriks on tyhi!!!")
                return 0
            if self.veer_arv() != m2.read_arv():
                print("Neid maatrikseid ei saa korrutada!!!!")
                return
            temp = []
            m = self.read_arv()
            n = m2.veer_arv()
            for i in range(m):
                temp.append([])
                for j in range(n):
                    temp[i].append(int(round(skalaar(self.vec(i),m2.transpoos().vec(j)),3)))
            return Maatriks(temp)
        if type(m2) is int or type(m2) is float:
            temp = []
            for i in range(self.read_arv()):
                temp.append([])
                for j in range(self.veer_arv()):
                    temp[i].append(self.M[i][j]*m2)
            return Maatriks(temp)
    
    def __rmul__(self, m2):
        if type(m2) is Maatriks:
            if self.read_arv() == [] or m2.read_arv() == 0:
                print("Maatriks on tyhi!!!")
                return 0
            if self.read_arv() != m2.veer_arv():
                print("Neid maatrikseid ei saa korrutada!!!!")
                return
            temp = []
            for i in range(self.read_arv()):
                temp.append([])
                for j in range(self.veer_arv()):
                    temp[i].append(self.M[i][j]*m2)
            return Maatriks(temp)
        if type(m2) is int or type(m2) is float:
            temp = []
            for i in range(self.read_arv()):
                temp.append([])
                for j in range(self.veer_arv()):
                    temp[i].append(self.M[i][j]*m2)
            return Maatriks(temp)

    def __add__(self,m2):
        if type(m2) is int or type(m2) is float:
            print("Sa ei saa maatrikseid ja numbreid liita")
            return
        if self.read_arv() != m2.read_arv() or self.veer_arv() != m2.veer_arv():
            print("Neid maatrikseid ei saa liita!!!!")
            return
        temp = []
        for i in range(self.read_arv()):
            temp.append([])
            for j in range(self.veer_arv()):
                temp[i].append(self.M[i][j]+m2.M[i][j])
        return Maatriks(temp)
