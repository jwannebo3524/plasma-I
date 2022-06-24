from operator import iadd
import numpy as np
#youve got to have a biasis,
#a way to evaluate it all

# [coff, name, arg1, arg2....]
class Solver:
    def AttemptConvergence(Var,Exp,Funcs= None,Defs = None,limit=99,randnum=10,range=10): #Attempt to solve an equation by symbolic fixed point analysis
        c = 0
        Funcs.append(Var)
        Defs.append([[0,""]])
        Rate0 = None
        while(c<limit):
            z = Eval(Exp,Funcs = Funcs,Defs=Defs)
            z0 = Defs[-1]
            Defs[-1] = z     
            c += 1
    def ConstMult(const,Exp): #multiply expression by constant
        c = 0
        while(c<len(Exp)):
            Exp[c][0] *= const
            c += 1
        return Exp
    def Sum(Exp1,Exp2): #add two expressions
        Out = Exp1
        c = 0
        while(c<len(Exp1)):
            c2 = 0
            while(c2<len(Exp2)):
                if(Exp1[c][1] == Exp2[c2][1]):
                    Out[c][0] += Exp2[c2][0]
                c2 += 1
            c += 1
        return Out
    def Eval(Exp,Funcs = None,Defs = None):
        if(not Funcs == None):
            c = 0
            while(c<len(Exp)):
                if(Exp[c][1] in Funcs):
                    i = Funcs.index(Exp)
                    c2 = 0
                    while(c2<len(Defs[i])):
                        Exp.append(Defs[i][c2])
                        Exp[-1][0] *= Exp[c][0]
                        c2 += 1
                    Exp.pop(c)
                    c -= 1
                elif(Exp[c][1][:3] == "CMD"):
                    try:
                        z = getattr(Solver,Exp[c][1][3:])
                        if()
                    except:


                c += 1
        Exp = Sum()
