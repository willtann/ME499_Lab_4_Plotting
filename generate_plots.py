#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_4_Plotting
from msd import MassSpringDamper
import matplotlib.pyplot as plt


""" Initial values and inputs of system for Problem 1 """
mass = 1.0  # mass
spring = 5.0  # spring constant
damper = 2.5  # damping ratio
t_in = 40.0  # end time
dt_in = 0.01  # time step size
x_in = 1  # initial position
x_dot_in = -1  # initial velocity

smd = MassSpringDamper(mass, spring, damper)
state, t = smd.simulate(x_in, x_dot_in, t_in, dt_in)
position = state[:, 0]
velocity = state[:, 1]

plt.plot(t, position)
plt.xlabel('Position')
plt.ylabel('Time')
plt.title('Spring-Damper System with MassSpringDamper ODE Model')
plt.grid()
plt.savefig('Problem1.png')
plt.show()
