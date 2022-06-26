import numpy as np
#youve got to have a biasis,
#a way to evaluate it all

# [coff, name, arg1, arg2....]
class Solver:
    def AttemptConvergence(Var,Exp,Funcs= None,Defs = None,limit=99,randnum=10,range=10,evallimit = 100): #Attempt to solve an equation by symbolic fixed point analysis
        #WARNING: No divergence detection!! Not guarenteed to converge!!! check your results!!!!

        Exp = Solver.ConstMult(0.001,Exp) #hopefully by minimizing the derivitive this improves the chance of convergence.
        c = 0
        Funcs.append(Var)
        Defs.append([[0,""]])
        Rate0 = None
        while(c<limit):
            z = Solver.Eval(Exp,Funcs = Funcs,Defs=Defs,maximum = evallimit)
            z0 = Defs[-1]
            Defs[-1] = z     
            c += 1
        z = Solver.ConstMult(1000,z) #see above comment. normalization.
        return z
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
    def Eval(Exp,Funcs = None,Defs = None,maximum = 200): #
        if(not Funcs == None):
            c = 0
            while(c<len(Exp) and c<maximum):
                if(Exp[c][1] in Funcs):
                    i = Funcs.index(Exp)
                    c2 = 0
                    while(c2<len(Defs[i])):
                        Exp.append(Defs[i][c2])
                        Exp[-1][0] *= Exp[c][0]
                        c2 += 1
                    Exp.pop(c)
                    c -= 1
                elif(Exp[c][1][:3] == "CMD"): #for custom functions including multiplication
                    try:
                        z = getattr(Solver,Exp[c][1][3:])
                        args = []
                        c2 = 2
                        while(c2<len(Exp[c])):
                            args.apppend(Exp[c])
                            c2 += 1
                        res,failed = z(args)
                        if(failed):
                            Exp.pop(c)
                            c -= 1
                        else:
                            try:
                                c2 = 0
                                while(c2<len(res)):
                                    f = len(res[c2])
                                    assert f>1
                                    Exp.append(res[c2])
                                    c2 += 1
                            except:
                                try:
                                    assert len(res)>1
                                    Exp.append(res)
                                except:
                                    print("Command "+Exp[c][1][3:]+" outputs in an incorrect format./n A term should be represented as [cofficient,value name, (optional arguments)..., ...]./n Use an empty string for a constant value name./n Use an array of these terms to form an expression.")
                    except:
                        print("Command "+ Exp[c][1][3:]+ " appears to be nonexistant or improperly configured.")
                c += 1
        Exp = Solver.ConstMult(0.5,Solver.Sum(Exp,Exp)) #combine like terms
