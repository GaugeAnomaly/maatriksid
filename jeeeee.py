from maatriksid import *

m = Maatriks([[1,2,3,4],
     [-3,-2,-3,-4],
     [8,-9,1,0],
     [0,-1,-2,2]])
print(m.korruta(m.pöörd()).det())
