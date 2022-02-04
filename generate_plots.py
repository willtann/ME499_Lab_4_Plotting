#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_4_Plotting
from msd import MassSpringDamper
from utils import simulate_gachapon
import matplotlib.pyplot as plt


""" Initial values of system for Problem 1: Spring Damper System """
mass = 1.0  # mass
spring = 5.0  # spring constant
damper = 2.5  # damping ratio
t_in = 40.0  # end time
dt_in = 0.01  # time step size
x_in = 1  # initial position
x_dot_in = -1  # initial velocity

# Using class MassSpringDamper from msd.py to model position and velocity over time with the inputs
smd = MassSpringDamper(mass, spring, damper)
state, t = smd.simulate(x_in, x_dot_in, t_in, dt_in)

# Plotting Problem 1
plt.plot(t, state[:, 0])  # first column of state is position
plt.xlabel('Position')
plt.ylabel('Time')
plt.title('Spring-Damper System with MassSpringDamper ODE Model')
plt.grid()
plt.savefig('Problem1.png')
plt.show()
# References:


""" Initial values of system for Problem 2: Histogram of the Gachapan """
n_prizes = 15  # Number of possible prizes
n_success = 1000  # Win all 15 prizes 1000 times
stats = []  # a place to store

for game in range(0, n_success):
    stats.append(simulate_gachapon(n_prizes))

n, bins, patches = plt.hist(stats, 50, facecolor='blue', alpha=0.5)
plt.xlabel('Happy Meals')
plt.ylabel('Probability')
plt.title('How many Happy Meals until you collect all 15 prizes?')
plt.grid()
plt.savefig('Problem2.png')
plt.show()
# References: https://pythonspot.com/matplotlib-histogram/
