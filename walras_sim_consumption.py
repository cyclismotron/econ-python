# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:42:16 2017

@author: 609687749
"""

from mesa import Agent, Model
from mesa.time import RandomActivation
import random
import matplotlib.pyplot as plt

class MoneyAgent(Agent):
    """An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id,model)
        self.alpha = random.uniform(0, 1)
        self.e1=int(random.uniform(1,10))
        self.e2=int(random.uniform(1,10))
        self.Uinit= float(self.e1**self.alpha * self.e2**(1-self.alpha))
        
    def step(self):
        #The agent's step will go here.
        self.x1dot = self.alpha * (model.p1*self.e1+model.p2*self.e2) / model.p1
        self.x2dot = (1-self.alpha) * (model.p1*self.e1+model.p2*self.e2) / model.p2
        self.Ufinal = self.x1dot**self.alpha*self.x2dot**(1-self.alpha)
        pass
        
class MoneyModel(Model):
    """A model with some number of agents."""
    def __init__(self, N, p1, p2):
        self.num_agents = N
        self.p1 = p1
        self.p2 = p2        
        self.schedule = RandomActivation(self)
        #Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)
            

    def step(self):
        '''Advance the model by one step'''
        self.schedule.step()
        self.x1dot_tot = sum(a.x1dot for a in model.schedule.agents)
        self.x2dot_tot = sum(a.x2dot for a in model.schedule.agents)
        self.e1_tot = sum(a.e1 for a in model.schedule.agents)
        self.e2_tot = sum(a.e2 for a in model.schedule.agents)
        self.U = sum(a.Ufinal for a in model.schedule.agents)
        self.z1 = self.x1dot_tot - self.e1_tot
        self.z2 = self.x2dot_tot - self.e2_tot
        print("Excess demand for good 1: ", round(self.z1,2)," and good 2: ", round(self.z2,2))
        print("Prices used for good 1: ", self.p1," and good 2: ", self.p2)
        print("Total Utility:",round(self.U,2))
        
        
        if self.z1>0:
            self.p1 = self.p1+1
        elif self.z1<0:
            self.p1 = self.p1-1
            
        if self.z2>0:
            self.p2 = self.p2+1
        elif self.z2<0:
            self.p2 = self.p2-1