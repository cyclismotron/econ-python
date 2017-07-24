# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:30:25 2017

@author: 609687749
"""
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random


#class agent(object):
#
#    def __init__(self):
#        print ("Set the parameters for your agent")
#        prompt = '> '
#        print ("What is alpha?"),
#        self.alpha = input(prompt)
#        print ("What is endowment of x1?"),
#        self.e1 = int(input(prompt))
#        print ("What is endowment of x2?"),
#        self.e2 = int(input(prompt) )

class agent_auto(object):

    def __init__(self):
        self.alpha = float()
        self.e1 = int()
        self.e2 = int()
        self.Uinit = float()
        self.Ufinal=float()
        
def sim_agents(n, x1_max,x2_max):
    agents_list = []
    a = random.uniform(0, 1)
    i=1
    while i<=n:
        agt_i = agent_auto()
        agt_i.alpha=a
        agt_i.e1=int(random.uniform(1,x1_max))
        agt_i.e2=int(random.uniform(1,x2_max))
        agents_list.append(agt_i)
        agt_i.Uinit= float(agt_i.e1**agt_i.alpha * agt_i.e2**(1-agt_i.alpha))
        i= i+1
    return(agents_list)
        
def prep():
    print("You are the Walrasian Auctioneer. It is your job to set the prices so that the market clears")
    print("How many people are in your market place?")
    prompt = '> '
    n = int(input(prompt))
    print("These people all have random preferences between two goods, x1 and x2")
    print("Before the market opens, they are all randomly endowed with an amount of each good")
    print("What is the maximum of x1 anyone will get?")
    x1_max = int(input(prompt))
    print("What is the maximum of x2 anyone will get?")
    x2_max = int(input(prompt))
    output = sim_agents(n,x1_max,x2_max)   
    return(output)
    
def trading(p1,p2,agent_pop):
    x1dot_list = []
    x2dot_list = []
    e1_list = []
    e2_list = []
    Uinit_list = []
    Ufinal_list=[]
    for agt in agent_pop:
        agt.x1dot = agt.alpha * (p1*agt.e1+p2*agt.e2) / p1
        agt.x2dot = (1-agt.alpha) * (p1*agt.e1+p2*agt.e2) / p2
        x1dot_list.append(agt.x1dot)
        x2dot_list.append(agt.x2dot)
        e1_list.append(agt.e1)
        e2_list.append(agt.e2)
        agt.Ufinal = agt.x1dot**agt.alpha*agt.x2dot**(1-agt.alpha)
        Uinit_list.append(agt.Uinit)
        Ufinal_list.append(agt.Ufinal)
        #print (agt.x1dot, agt.x2dot)
    
    z1 = sum(x1dot_list) - sum(e1_list)
    z2 = sum(x2dot_list) - sum(e2_list)
    Uinit = sum(Uinit_list)
    Ufinal = sum(Ufinal_list)
    return round(z1,2), round(z2,2), round(Uinit,2), round(Ufinal,2)
    
def price_set(agent_list):
    prompt= '> '    
    print("What price would you like to set for good 1?")
    p1 = float(input(prompt))
    print("and what price would you like to set for good 2?")
    p2 = float(input(prompt))    
    output = trading(p1,p2,agent_list)    

    if output[0]>0:
        print("after trading has finished, there is not enough of good 1:")
        print("shortage",output[0])
    elif output[0]<0:
        print("after trading has finished, there is too much of good 1:")
        print("surplus",-output[0])
    
    if output[1]>0:
        print("after trading has finished, there is not enough of good 2:")
        print("shortage",output[1])
    elif output[1]<0:
        print("after trading has finished, there is too much of good 2:")
        print("surplus",-output[1])
    
    if (float(output[3]) - float(output[2]))>0:
        print("and people were this much happier in total after trading:")
        float(output[3]) - float(output[2])
    elif (float(output[3]) - float(output[2]))<0:
        print("and people were this much less happy in total after trading:")
        -(float(output[3]) - float(output[2]))
    
    print("Do you want to try some different prices? Y, or N")
    response = str()    
    response = input(prompt)
    
    if response == "Y":
        price_set(agent_list)

def excessdemand():
    
    pop = prep()
    print(len(pop))
    price_set(pop)     

        
def simulate():

    ed = []
    parms = []
    for i in range (1,100):
        for j in range (1,100):
            p = [i/10,j/10]
            parms.append(p)
            ed.append(excessdemand(i/10,j/10))
    ed_df = pd.DataFrame(ed)
    parms_df = pd.DataFrame(parms)
    output = pd.concat([ed_df,parms_df], axis=1)
    output.columns = ['ed_x1','ed_x2','U_init','U_final','p1','p2']
  
    output = pd.concat([output,abs(output.ed_x1) + abs(output.ed_x2)], axis=1)
    
    output.columns = ['ed_x1','ed_x2','U_init','U_final','p1','p2','aggd']
    
   # fig = plt.figure()
   # ax=Axes3D(fig)
   # ax.set_xlabel('p1')
   # ax.set_ylabel('p2')
   # ax.set_zlabel('Excess demand for x2')
   # ax.set_title('Prices and Total Excess Demand')
   # ax.scatter(output.p1,output.p2,output.aggd)
    
    return output
        