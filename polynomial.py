from utility.reverseEnum import reverseEnumerate

def coeffToString(a,Supress1=True):
    res=''
    if Supress1 and abs(round(a,3)-1)==0:
        return res

    if a<0:
        res+='-'
        a*=-1

    if abs(round(a,3)-round(a,0))==0:
        res+=str(int(a+0.5))
    else:
        res+=str(round(a,3))
    return res

class Polynomial:
    def __init__(self,coeffs):
        self.A=coeffs
    def __str__(self):
        res=""
        for p, a in reverseEnumerate(self.A):
            if a==0:
                continue

            #print(a,p)

            if p<len(self.A)-1 and a>0:
                res+='+'

            if p==0:
                res+=coeffToString(a,Supress1=False)
            elif p==1:
                res+=coeffToString(a)+'x'
            else:
                res+="{}x^{}".format(coeffToString(a),p)

        return res

    def __call__(self, x):
        res=0
        for p,a in enumerate(self.A):
            res+=a*(x**p)
        return res