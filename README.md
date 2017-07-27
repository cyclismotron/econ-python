# econ-python


This is a collection of toy models built to develop my Python skills
and revise key topics in economics

Walras

This game illustrates Walrasion equilibrium in a pure exchange market. Users can choose the number of market agents, who all have homogeneous degree 0 Cobb-Douglas preferences.  Each agent is randomly allocated an endowment of the two goods.  The user can then specify a price vector and the model then calculates the excess demand of the two goods.

The command "excessdemand()" executes the model.

Walras Sim

This is a simulation of pure exchange market, where the user specifies the number of agents and initial prices. Prices then adjust over a number of periods in 0.1 increments.

Outputs illustrate how excess demand approaches zero and what the implied market-clearing prices are for each of the two goods.

Walras Sim Solve

This simulation automatically solves for the equilibrium price ratio, given a number of agents, maximum values for goods 1 and 2, and mean preference for good 1.

To run it simply import the code use the command solve(sim_agents(N,x1max,x2max,mean preference)).

This function prints the price ratio and some graphs, and returns a dataframe containing the details of the agents (preference for good 1, initial endowments and final wealth).