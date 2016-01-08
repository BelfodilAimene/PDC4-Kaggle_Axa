import os
import random
from yahmm import *
class ModelGenerator :
    def __init__(self,statesNumber=6) :
        self.statesNumber=statesNumber
        random.seed(0)
    def generateModel(self,modelName) :
        self.distribution = UniformDistribution(0.0, 1.0)
        model= Model(name=modelName)
        states=[]
        for i in range(self.statesNumber) :
            state=State(self.distribution,name="state"+str(i))
            states.append(state)
            model.add_state(state)
            model.add_transition(model.start,state,1/float(self.statesNumber))
            model.add_transition(state,model.end,0.2)
        for stateI in states :
            for stateJ in states :
                model.add_transition(stateI,stateJ,0.8/float(self.statesNumber))
        model.bake()
        return model
                
            

        
        
        
