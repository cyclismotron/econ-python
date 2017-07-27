# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:09:10 2017

@author: 609687749
"""
import matplotlib.pyplot as plt
import random
from   scipy.optimize import fsolve
import pandas as pd

## define our agent class
class agent_auto(object):

    def __init__(self):
        self.alpha = float()
        self.e1 = int()
        self.e2 = int()        
        self.x1dot = lambda p: self.alpha * (self.e1+p*self.e2)
        self.x2dot = lambda p: (1-self.alpha) * (self.e1+p*self.e2)
        
        
  #  def x1dot(self, p1, p2):
  #      return self.alpha * (p1*self.e1+p2*self.e2) / p1
        
   # def x2dot(self, p1, p2):
    #    return (1-self.alpha) * (p1*self.e1+p2*self.e2) / p2

##populate agents_list with a bunch agent_auto objects      
def sim_agents(n, x1_max,x2_max, a_mean):
    agents_list = []
    i=1
    while i<=n:
        agt_i = agent_auto()
        agt_i.alpha=random.gauss(mu=a_mean, sigma=0.1)
        if agt_i.alpha<=0:
            agt_i.alpha = 0.001
        elif agt_i.alpha>=1:
            agt_i.alpha=0.999
        agt_i.e1=int(random.uniform(1,x1_max))
        agt_i.e2=int(random.uniform(1,x2_max))
        agents_list.append(agt_i)
        i= i+1
    return(agents_list)
    
def sigma(funcs,p):
    return sum(f(p) for f in funcs)
    
    
def solve(pop): 
# First, make lists of x1dot ftns    
    x1dot_list=[]
#    x2dot_list=[]
#    e2_list=[]
#    
    for i in pop:
        x1dot_list.append(i.x1dot)
#        x2dot_list.append(i.x2dot())
#        e2_list.append(i.e1)
       
# Set up aggregate demand function
    z1 = lambda p: sigma(x1dot_list,p) - sum(a.e1 for a in pop)

# Minimise aggregate demand
    price_ratio = fsolve(z1,1)
    
    agents_alpha = pd.DataFrame(a.alpha for a in pop)
    agents_e1 = pd.DataFrame(a.e1 for a in pop)
    agents_e2 = pd.DataFrame(a.e2 for a in pop)
    
    agents_df = pd.concat([agents_alpha, agents_e1, agents_e2], axis=1)
    
    agents_df.columns = ['alpha','e1','e2']
    agents_df.wealth = agents_df.e1 + agents_df.e2 * price_ratio[0]
    
    fig = plt.figure()
    sp1 = fig.add_subplot(2,2,1)
    sp1.hist(agents_df.alpha)
    sp2 = fig.add_subplot(2,2,2)
    sp2.hist(agents_df.wealth)
    sp3 = fig.add_subplot(2,2,3)    
    sp3.scatter(agents_df.alpha,agents_df.wealth)    
    
    print("Price ratio p2/p1:",round(price_ratio[0],2))

    return(agents_df)
