# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 16:46:05 2017

@author: 609687749
"""

from walras_sim_consumption import *

## set up the model with N agents, and initial prices for good 1 and good 2.
model = MoneyModel(1000,10,2)
for i in range(100):
    model.step()

## Did consumers have a bigger preference for good 1 or good 2?
## (Lower values for alpha mean a preference for good 2)
agents_data = model.datacollector.get_agent_vars_dataframe()
fig2 = plt.figure()
alpha = fig2.add_subplot(1,1,1)
alpha.hist(agents_data["Alpha"])
fig2

##The less preferred good should end up with a lower price...
modeldata = model.datacollector.get_model_vars_dataframe()
fig = plt.figure()
ed = fig.add_subplot(2,1,1)
ed.plot(modeldata["ExcessGood1"], label = 'Excess Demand: Good 1')
ed.plot(modeldata["ExcessGood2"], label = 'Excess Demand: Good 2')
ed.legend(loc='best')
p = fig.add_subplot(2,1,2)
p.plot(modeldata["PriceGood1"], label = 'Price: Good 1')
p.plot(modeldata["PriceGood2"], label = 'Price: Good 2')
p.legend(loc='best')

fig

