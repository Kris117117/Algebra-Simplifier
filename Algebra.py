import sys
string="3x*2+x^3+5x+x" #Example equation for now, will eventually be a input statement from user
var='0'
for i in range(len(string)):
    if string[i].isalpha():
        var=string[i]
        break
if not var.isalpha():
    print(eval(string))
    sys.exit()
print(var)
class term:
    def __init__(self,string,var):
        varIndex=string.find(var)
        if varIndex==-1:
            self.coef=float(string)
            self.degree=0
            self.var=None
        else:
            self.var=var
            coefPart=string[:varIndex]
            if len(coefPart)>0:
                if coefPart == '-':
                    self.coef=-1
                else:
                    self.coef=float(coefPart)
            else:
                self.coef=1
            degreePart=string[varIndex+1:]
            if len(degreePart)>0:
                self.degree=float(degreePart[1:])
            else:
                self.degree=1
            if string.find('^') == -1:
                self.coef*=self.degree
                self.degree=1

signs=('+','-','*','/')
lst=[]
num=0
for i in range(len(string)):
    if string[i] in signs:
        lst.append(string[num:i])
        lst.append(string[i])
        num=i+1
lst.append(string[num:])
print(lst)
def findTypeVar(string):
    var='0'
    for i in range(len(string)):
        if string[i].isalpha():
            var=string[i]
            break
    return var
varlst=[]
for i in range(len(lst)):
    if lst[i] not in signs:
        varlst.append(term(lst[i],findTypeVar(lst[i])))
for i in range(len(varlst)):
    classVar=varlst[i]
    print(classVar.coef,classVar.degree)
