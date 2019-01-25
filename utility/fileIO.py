from csv import reader, writer
from numpy import array

def matrixFromDump(dump,topLeft,botRight):
    if not topLeft[0]<botRight[0] or not topLeft[1]<botRight[1]:
        return None
    try:
        trimed=[list(map(lambda x:float(x),row[topLeft[0]:botRight[0]])) for row in dump[topLeft[1]:botRight[1]]]
        return array(trimed)
    except:
        return None

def loadDimentionalPoints(path):
    return list(map(lambda l:tuple(l),CSVLoad(path)))

def saveDimentionalPoints(data,path):
    CSVSave(list(map(lambda t:list(t),data)),path)

def CSVLoad(path):
    res=[]
    with open(path,mode='r') as file:
        csv=reader(file)
        for row in csv:
            r=[]
            for cell in row:
                try:
                    r.append(float(cell))
                except:
                    r.append(cell)
            res.append(r)
    return res

def CSVSave(data,path):
    with open(path,mode='w') as file:
        csv=writer(file,lineterminator='\n')
        for row in data:
            csv.writerow(row)