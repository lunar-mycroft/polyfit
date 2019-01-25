from numpy import  matmul, std
from numpy.linalg import inv as invert

from utility.fileIO import matrixFromDump,CSVLoad
from utility.reverseEnum import reverseEnumerate

class polynomial:
    def __init__(self,coeffs):
        self.A=coeffs
    def __str__(self):
        res=""
        for p, a in reverseEnumerate(self.A):
            if p==0:
                res+=str(round(abs(a) if p+1<len(self.A) else a,3))
            elif p==1:
                res+=str(round(abs(a) if p+1<len(self.A) else a,3))+'x'
            else:
                res+="{}x^{}".format(round(abs(a) if p+1<len(self.A) else a,3),p)
            
            if p>0:
                res+='+' if self.A[p-1]>0 else '-'

        return res

    def __call__(self, x):
        res=0
        for p,a in enumerate(self.A):
            res+=a*(x**p)
        return res

def sum2Power(data,power):
    if power==0:
        return len(data)
    if power==1:
        return sum(data)
    return sum(map(lambda x:x**power,data))

def regressVectorTerm(data,power):
    if power==0:
        return sum(map(lambda x: x[1],data))

    return sum(map(lambda x: x[1]*(x[0]**power),data))

def regressVector(data,degree):
    result=[]
    for i in range(0,degree+1):
        result.append(regressVectorTerm(data,i))
    return result

def regressMatrix(data,degree):
    result=[]
    for i in range(0,degree+1):
        row=[]
        for j in range(0,degree+1):
            row.append(sum2Power(data,i+j))
        result.append(row)
    return result

def rSquared(data,poly):
    Y=[y for y in map(lambda p:p[1],data)]
    DeltaY=[dY for dY in map(lambda p:poly(p[0])-p[1],data)]

    return 1-std(DeltaY)/std(Y)

def polyFit(data,degree):
    if len(data)<degree:
        return 1, None
    if len(data)<2*degree:
        return 2, None
    xOnly=list(map(lambda x:x[0],data))

    poly=polynomial(matmul(regressVector(data,degree),invert(regressMatrix(xOnly,degree))))

    return None, poly, rSquared(data,poly)


fit=polyFit(matrixFromDump(CSVLoad('u6vsLFP.csv'),(1,1),(3,301)),2)

print(fit[1],fit[2])

