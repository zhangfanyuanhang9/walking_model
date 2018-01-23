
from numpy import sin, cos
import numpy as np
import dynamics
import matplotlib.pyplot as plt
from math import pi
import scipy.integrate as integrate
import matplotlib.animation as animation
import Subject
plt.ion()
class Plotter():

    def __init__(self):
        self.fig = plt.figure()
        ax = self.fig.add_subplot(111, autoscale_on=False, xlim=(-7, 7), ylim=(-7, 7))
        ax.grid()

        self.back_leg, = ax.plot([], [], 'bo-', lw=2)
        self.front_leg, = ax.plot([], [], 'ro-', lw=2)
        self.trunk, = ax.plot([], [], 'go-', lw=2)
        #plt.show()


    def update(self, sub):
        points = dynamics.FK(sub)
        back = [ _.tolist() for _ in points[:3]]
        flat_back = [item for sublist in back for item in sublist]
        front = [_.tolist() for _ in points[3:]]
        flat_front = [item for sublist in front for item in sublist]
        print flat_front
        self.back_leg.set_ydata([ flat_back[1], flat_back[3], flat_back[5] ])
        self.back_leg.set_xdata([ flat_back[0], flat_back[2], flat_back[4] ])

        self.front_leg.set_ydata([flat_back[5],flat_front[1], flat_front[3]])
        self.front_leg.set_xdata([flat_back[4],flat_front[0], flat_front[2]])

        self.trunk.set_ydata([flat_back[5], flat_front[5]])
        self.trunk.set_xdata([flat_back[4], flat_front[4]])

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


        #
        # pass