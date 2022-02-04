#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_4_Plotting
from msd import MassSpringDamper
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


""" Initial values of system for Problem 2: Histogram of the Gachapan """
