import numpy as np
import mircosimI as ms

class Edge_Feild_Simulation:
    def __init__(self,dimx,dimy,dimz,resX,resT,species,):
        #species format:  [name,mass,neuclear charge(s),net charge,bond strength, decay products]
        # 
        self.dimx,self.dimy,self.dimz = dimx,dimy,dimz
        self.resX,self.resT = resX,resT
