#! /Users/tannerwilliams/Desktop/ME 499/ME499_Lab_4_Plottinsg
from msd import MassSpringDamper


def time_position(mass=1.0, spring=1.0, damp=1.0, run_time=100.0, dt_in=0.01, x_in=0.0, x_dot_in=0.0):
    # use clss MassSpringDamper from import
    system = MassSpringDamper(mass, spring, damp)
    state, times = system.simulate(x_in, x_dot_in, run_time, dt_in)
    return state, times
