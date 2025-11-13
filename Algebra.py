import sys
string="3/2x-x^3+5x+x+2+325+3y^(x-1)-2y^(x-1)+2y(x(x+1))^2"
class term:
    def __init__(self,string,var):
        varIndex=string.find(var)
        if varIndex==-1:
            self.coef=float(string)
            self.degree='^0'
            self.var='x'
        else:
            self.var=var
            coefPart=string[:varIndex]
            if len(coefPart)>0:
                if coefPart == '-':
                    self.coef=-1
                else:
                    self.coef=eval(coefPart)
            else:
                self.coef=1
            #degree part
            degreePart=string[varIndex+1:]
            if len(degreePart)>0:
                self.degree=degreePart
            else:
                self.degree='^1'

lst=[]
num=0
stop=False
for i in range(len(string)):
    if string[i]=='(':
        stop=True
    elif string[i]==')':
        stop=False
    if not stop:
        if string[i] == '+':
            lst.append(string[num:i])
            lst.append('+')
            num=i+1
        elif string[i]=='-':
            lst.append(string[num:i])
            lst.append('+')
            num=i

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
    if lst[i] != '+':
        varlst.append(term(lst[i],findTypeVar(lst[i])))
print('\n')

def combineLikeTerms(lst):
    combined = {}
    for t in lst:
        key = (t.var, t.degree)
        if key in combined:
            combined[key] += t.coef
        else:
            combined[key] = t.coef

    newlst = []
    for (var, degree), coef in combined.items():
        term_str = f"{coef}{var}{degree}"
        newlst.append(term(term_str, var))
    return newlst


newlst = combineLikeTerms(varlst)

for num in newlst:
    print(str(num.coef)+str(num.var)+str(num.degree))

